"""Прогон обработчиков бота с поддельными Update/Context, без сети."""
import asyncio
from types import SimpleNamespace
from unittest.mock import AsyncMock

from mira import bot
from mira.coach import Coach
from mira.config import Settings
from mira.db import Database


class FakeClient:
    def __init__(self):
        self.messages = self
        self.calls = []

    async def create(self, **kw):
        self.calls.append(kw)
        return SimpleNamespace(content=[SimpleNamespace(type="text", text="Hi, I'm here.")])


def make_env():
    settings = Settings(telegram_token="x", anthropic_api_key="y", paywall_enabled=False)
    db = Database(":memory:")
    client = FakeClient()
    services = bot.Services(settings, db, Coach(client, settings, db))
    ctx = SimpleNamespace(
        application=SimpleNamespace(bot_data={"svc": services}),
        bot=SimpleNamespace(send_chat_action=AsyncMock(), send_message=AsyncMock()),
        args=[],
    )
    return services, ctx, client


def make_update(text=None, data=None, user_id=42):
    sent = []

    async def reply_text(t, reply_markup=None):
        sent.append(t)

    msg = SimpleNamespace(text=text, reply_text=reply_text)
    upd = SimpleNamespace(
        effective_user=SimpleNamespace(id=user_id),
        effective_chat=SimpleNamespace(id=user_id),
        effective_message=msg,
        callback_query=SimpleNamespace(data=data, message=msg, answer=AsyncMock()) if data else None,
    )
    return upd, sent


def run(coro):
    return asyncio.run(coro)


def test_full_onboarding_then_chat_and_safety():
    s, ctx, client = make_env()

    run(bot.cmd_start(*[make_update("/start")[0], ctx]))
    for data in ["lang:ru", "age:yes"]:
        run(bot.on_button(make_update(data=data)[0], ctx))
    for text in ["Дан"]:
        run(bot.on_text(make_update(text)[0], ctx))
    run(bot.on_button(make_update(data="goal:cut_back")[0], ctx))
    for text in ["14", "красное вино", "по вечерам", "бросал, не вышло", "сон"]:
        run(bot.on_text(make_update(text)[0], ctx))

    user = s.db.get_user(42)
    assert user["step"] == "done" and user["lang"] == "ru" and user["baseline_per_week"] == 14
    assert "Russian" in client.calls[-1]["system"][1]["text"]  # welcome ушёл с русским языком

    n_calls = len(client.calls)
    upd, sent = make_update("Хочу выпить")
    run(bot.on_text(upd, ctx))
    assert sent == ["Hi, I'm here."] and len(client.calls) == n_calls + 1

    # кризис: ответ без обращения к модели
    upd, sent = make_update("не хочу жить")
    run(bot.on_text(upd, ctx))
    assert "ЭРАН" in sent[0] and len(client.calls) == n_calls + 1

    upd, sent = make_update()
    ctx.args = ["2", "вино"]
    run(bot.cmd_log(upd, ctx))
    assert "2" in sent[0]


def test_under_18_is_blocked():
    s, ctx, client = make_env()
    run(bot.cmd_start(make_update("/start")[0], ctx))
    run(bot.on_button(make_update(data="lang:en")[0], ctx))
    run(bot.on_button(make_update(data="age:no")[0], ctx))
    upd, sent = make_update("hello")
    run(bot.on_text(upd, ctx))
    assert "adults" in sent[0] and client.calls == []


def test_rate_limit_and_paywall():
    s, ctx, client = make_env()
    run(bot.cmd_start(make_update("/start")[0], ctx))
    s.db.update_user(42, step="done", lang="en", name="Dan")
    object.__setattr__(s.settings, "daily_message_limit", 2)
    for _ in range(2):
        run(bot.on_text(make_update("hi")[0], ctx))
    upd, sent = make_update("hi again")
    run(bot.on_text(upd, ctx))
    assert "tomorrow" in sent[0]

    object.__setattr__(s.settings, "paywall_enabled", True)
    s.db.update_user(42, trial_ends_at="2000-01-01T00:00:00+00:00")
    upd, sent = make_update("hi")
    run(bot.on_text(upd, ctx))
    assert "trial has ended" in sent[0]


def test_build_app_registers_handlers():
    app = bot.build_app(Settings(telegram_token="123:abc", anthropic_api_key="k", db_path=":memory:"))
    assert app.bot_data["svc"] and app.job_queue is not None
