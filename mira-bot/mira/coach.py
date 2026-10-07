"""Вызовы Claude: контекст пользователя, выбор модели, история диалога."""

import logging
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from . import prompts
from .config import Settings
from .db import Database, now_utc, parse_iso

log = logging.getLogger(__name__)

HISTORY_LIMIT = 24
MODE_TTL = timedelta(hours=3)


def effective_mode(user) -> str:
    """Режим живёт 3 часа после установки, потом возвращаемся в general."""
    mode = user["mode"] or "general"
    set_at = parse_iso(user["mode_set_at"])
    if mode != "general" and (set_at is None or now_utc() - set_at > MODE_TTL):
        return "general"
    return mode


def profile_summary(user) -> str:
    goal = {"cut_back": "cut back", "break": "30-day break", "quit": "quit for good"}.get(
        user["goal"], user["goal"] or "unknown"
    )
    lines = [
        f"Name: {user['name'] or 'unknown'}",
        f"Goal: {goal}",
        f"Typical drinks per week before starting: {user['baseline_per_week']}",
        f"Usual drink: {user['drink'] or 'unknown'}",
        f"Triggers (their words): {user['triggers'] or 'unknown'}",
        f"Tried before (their words): {user['tried'] or 'unknown'}",
        f"Why now (their words): {user['motivation'] or 'unknown'}",
    ]
    return "\n".join(lines)


def normalize_history(rows: list[dict]) -> list[dict]:
    """Склеивает подряд идущие реплики одной роли, гарантирует старт с user."""
    merged: list[dict] = []
    for r in rows:
        if merged and merged[-1]["role"] == r["role"]:
            merged[-1]["content"] += "\n" + r["content"]
        else:
            merged.append({"role": r["role"], "content": r["content"]})
    if merged and merged[0]["role"] == "assistant":
        merged.insert(0, {"role": "user", "content": "(conversation resumed)"})
    return merged


class Coach:
    def __init__(self, client, settings: Settings, db: Database):
        self.client = client
        self.settings = settings
        self.db = db

    def _recent_summary(self, user) -> str:
        end = now_utc()
        week = self.db.drinks_total(user["tg_id"], end - timedelta(days=7), end)
        today = self.db.drinks_total(user["tg_id"], end - timedelta(hours=24), end)
        return f"Logged drinks: last 24h = {today:g}, last 7 days = {week:g}."

    def _system(self, user, mode: str) -> list[dict]:
        tz = ZoneInfo(user["tz"] or self.settings.default_tz)
        now_local = datetime.now(tz).strftime("%A %H:%M")
        dyn = prompts.dynamic_prompt(
            profile=profile_summary(user),
            recent_summary=self._recent_summary(user),
            now_local=now_local,
            mode=mode,
            lang=user["lang"] or "en",
        )
        return prompts.system_blocks(dyn)

    async def _call(self, model: str, system: list[dict], messages: list[dict], max_tokens: int) -> str:
        resp = await self.client.messages.create(
            model=model, max_tokens=max_tokens, system=system, messages=messages
        )
        text = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text").strip()
        if not text:
            raise RuntimeError("empty model response")
        return text

    async def reply(self, user, text: str, mode: str) -> str:
        """Ответ на сообщение пользователя. Сообщение уже сохранено в БД."""
        rows = [dict(r) for r in self.db.recent_messages(user["tg_id"], HISTORY_LIMIT)]
        messages = normalize_history(rows)
        if not messages or messages[-1]["role"] != "user":
            messages.append({"role": "user", "content": text})
        model = self.settings.model_sos if mode == "sos" else self.settings.model_chat
        max_tokens = 900 if mode == "sos" else 500
        return await self._call(model, self._system(user, mode), messages, max_tokens)

    async def opener(self, user, mode: str) -> str:
        """Проактивное сообщение (чек-ин, приветствие)."""
        rows = [dict(r) for r in self.db.recent_messages(user["tg_id"], 12)]
        messages = normalize_history(rows)
        instruction = prompts.OPENER_INSTRUCTIONS[mode]
        if messages and messages[-1]["role"] == "user":
            messages[-1]["content"] += "\n\n" + instruction
        else:
            messages.append({"role": "user", "content": instruction})
        return await self._call(self.settings.model_chat, self._system(user, mode), messages, 400)

    async def weekly_report(self, user, facts: str) -> str:
        messages = [{"role": "user", "content": prompts.REPORT_INSTRUCTION.format(facts=facts)}]
        return await self._call(self.settings.model_report, self._system(user, "general"), messages, 500)
