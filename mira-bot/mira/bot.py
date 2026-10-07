"""Telegram-обработчики. Логика вынесена в соседние модули, здесь только склейка."""

import logging
from dataclasses import dataclass
from datetime import timedelta
from zoneinfo import ZoneInfo

import anthropic
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ChatAction
from telegram.ext import (
    Application, CallbackQueryHandler, CommandHandler, ContextTypes, MessageHandler, filters,
)

from . import onboarding, safety, schedule
from .coach import Coach, effective_mode
from .config import Settings
from .db import Database, iso, now_utc
from .i18n import t

log = logging.getLogger("mira")

TICK_SECONDS = 900


@dataclass
class Services:
    settings: Settings
    db: Database
    coach: Coach


def svc(ctx: ContextTypes.DEFAULT_TYPE) -> Services:
    return ctx.application.bot_data["svc"]


def kb(rows: list[list[tuple[str, str]]]) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(label, callback_data=data) for label, data in row] for row in rows]
    )


def lang_of(user) -> str:
    return (user["lang"] if user else None) or "en"


async def say(update: Update, text: str, markup=None) -> None:
    await update.effective_message.reply_text(text, reply_markup=markup)


async def ask_current_step(update: Update, user) -> None:
    """Задаёт вопрос текущего шага онбординга."""
    lang, step = lang_of(user), user["step"]
    if step == "lang":
        await say(update, t("en", "choose_lang") + "\n" + t("ru", "choose_lang"),
                  kb([[("English", "lang:en"), ("Русский", "lang:ru")]]))
    elif step == "age":
        await say(update, t(lang, "age"),
                  kb([[(t(lang, "age_yes"), "age:yes"), (t(lang, "age_no"), "age:no")]]))
    elif step == "goal":
        await say(update, t(lang, "q_goal", name=user["name"]),
                  kb([[(t(lang, "goal_cut_back"), "goal:cut_back")],
                      [(t(lang, "goal_break"), "goal:break")],
                      [(t(lang, "goal_quit"), "goal:quit")]]))
    elif step in onboarding.QUESTION_KEY:
        await say(update, t(lang, onboarding.QUESTION_KEY[step]))


# ---------- команды ----------

async def cmd_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    s = svc(ctx)
    tg_id = update.effective_user.id
    user = s.db.get_user(tg_id) or s.db.create_user(tg_id, s.settings.default_tz, s.settings.trial_days)
    if user["step"] == "done":
        await say(update, t(lang_of(user), "help"))
    else:
        await ask_current_step(update, user)


async def cmd_help(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    user = svc(ctx).db.get_user(update.effective_user.id)
    await say(update, t(lang_of(user), "help"))


async def require_ready(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    """Возвращает пользователя, если онбординг завершён и доступ есть, иначе отвечает и даёт None."""
    s = svc(ctx)
    user = s.db.get_user(update.effective_user.id)
    if user is None:
        await say(update, t("en", "need_start"))
        return None
    if user["step"] != "done":
        await ask_current_step(update, user)
        return None
    if not schedule.has_access(user, s.settings, now_utc()):
        await say(update, t(lang_of(user), "expired", link=s.settings.payment_link or "-"))
        return None
    return user


async def cmd_sos(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    s = svc(ctx)
    user = await require_ready(update, ctx)
    if not user:
        return
    lang = lang_of(user)
    s.db.update_user(user["tg_id"], mode="sos", mode_set_at=iso(now_utc()))
    s.db.start_sos(user["tg_id"])
    text = t(lang, "sos_start")
    s.db.add_message(user["tg_id"], "assistant", text, "sos")
    await say(update, text, kb([[(t(lang, "sos_ok"), "sos:ok")]]))


async def cmd_log(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    s = svc(ctx)
    user = await require_ready(update, ctx)
    if not user:
        return
    lang = lang_of(user)
    args = ctx.args or []
    try:
        count = float(args[0].replace(",", "."))
        if not 0 < count <= 50:
            raise ValueError
    except (IndexError, ValueError):
        await say(update, t(lang, "log_usage"))
        return
    drink = " ".join(args[1:]) or None
    s.db.log_drink(user["tg_id"], count, drink)
    end = now_utc()
    today = s.db.drinks_total(user["tg_id"], end - timedelta(hours=24), end)
    await say(update, t(lang, "logged", count=count, drink=drink or "", today=today).replace("  ", " "))


async def cmd_stats(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    s = svc(ctx)
    user = await require_ready(update, ctx)
    if not user:
        return
    lang = lang_of(user)
    end = now_utc()
    total = s.db.drinks_total(user["tg_id"], end - timedelta(days=7), end)
    key, pct = schedule.stats_delta(total, user["baseline_per_week"])
    delta = t(lang, key, pct=pct) if key != "delta_unknown" else ""
    await say(update, t(lang, "stats", total=total, baseline=user["baseline_per_week"] or "?", delta=delta).strip())


async def cmd_lang(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    await say(update, "Language / Язык:", kb([[("English", "lang:en"), ("Русский", "lang:ru")]]))


async def cmd_timezone(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    s = svc(ctx)
    user = s.db.get_user(update.effective_user.id)
    if not user:
        await say(update, t("en", "need_start"))
        return
    lang = lang_of(user)
    name = (ctx.args or [""])[0]
    try:
        ZoneInfo(name)
    except Exception:
        await say(update, t(lang, "tz_bad"))
        return
    s.db.update_user(user["tg_id"], tz=name)
    await say(update, t(lang, "tz_set", tz=name))


async def cmd_delete(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    user = svc(ctx).db.get_user(update.effective_user.id)
    lang = lang_of(user)
    await say(update, t(lang, "delete_confirm"),
              kb([[(t(lang, "delete_yes"), "del:yes"), (t(lang, "delete_no"), "del:no")]]))


async def cmd_grant(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    """Админская выдача доступа вручную: /grant <tg_id> <дней>. Нужна, пока нет оплаты."""
    s = svc(ctx)
    if update.effective_user.id not in s.settings.admin_ids:
        return
    try:
        target, days = int(ctx.args[0]), int(ctx.args[1])
    except (IndexError, ValueError):
        await say(update, "Usage: /grant <tg_id> <days>")
        return
    if not s.db.get_user(target):
        await say(update, "No such user")
        return
    s.db.update_user(target, paid_until=iso(now_utc() + timedelta(days=days)))
    await say(update, f"OK: {target} +{days}d")


# ---------- кнопки ----------

async def on_button(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    s = svc(ctx)
    q = update.callback_query
    await q.answer()
    tg_id = update.effective_user.id
    kind, _, value = q.data.partition(":")
    user = s.db.get_user(tg_id) or s.db.create_user(tg_id, s.settings.default_tz, s.settings.trial_days)
    lang = lang_of(user)

    if kind == "lang" and value in ("en", "ru"):
        s.db.update_user(tg_id, lang=value)
        user = s.db.get_user(tg_id)
        if user["step"] == "lang":
            s.db.update_user(tg_id, step="age")
            await ask_current_step(update, s.db.get_user(tg_id))
        else:
            await q.message.reply_text(t(value, "lang_set"))
    elif kind == "age" and user["step"] == "age":
        if value == "yes":
            s.db.update_user(tg_id, step="name")
            await ask_current_step(update, s.db.get_user(tg_id))
        else:
            s.db.update_user(tg_id, step="blocked")
            await q.message.reply_text(t(lang, "age_blocked"))
    elif kind == "goal" and user["step"] == "goal" and value in ("cut_back", "break", "quit"):
        s.db.update_user(tg_id, goal=value, step="baseline")
        await ask_current_step(update, s.db.get_user(tg_id))
    elif kind == "sos" and value == "ok":
        await q.message.reply_text(
            t(lang, "sos_done_ask"),
            reply_markup=kb([[(t(lang, "out_resisted"), "out:resisted"), (t(lang, "out_drank"), "out:drank"),
                              (t(lang, "out_unclear"), "out:unclear")]]),
        )
    elif kind == "out" and value in ("resisted", "drank", "unclear"):
        s.db.end_latest_sos(tg_id, value)
        s.db.update_user(tg_id, mode="general")
        await q.message.reply_text(t(lang, "sos_closed"))
    elif kind == "del" and value == "yes":
        s.db.delete_user(tg_id)
        await q.message.reply_text(t(lang, "deleted"))
    elif kind == "del":
        await q.message.reply_text(t(lang, "cancelled"))


# ---------- текст ----------

async def finish_onboarding(update: Update, ctx: ContextTypes.DEFAULT_TYPE, user) -> None:
    s = svc(ctx)
    tg_id, lang = user["tg_id"], lang_of(user)
    today = now_utc().astimezone(ZoneInfo(user["tz"] or s.settings.default_tz)).date().isoformat()
    s.db.update_user(tg_id, step="done", last_morning_date=today, last_evening_date=today)
    if onboarding.is_heavy(user["baseline_per_week"]):
        await say(update, t(lang, "heavy_warning"))
    user = s.db.get_user(tg_id)
    try:
        text = await s.coach.opener(user, "welcome")
    except Exception:
        log.exception("welcome failed")
        text = t(lang, "help")
    s.db.add_message(tg_id, "assistant", text, "general")
    await say(update, text)


async def on_text(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    s = svc(ctx)
    tg_id = update.effective_user.id
    text = update.effective_message.text or ""
    user = s.db.get_user(tg_id)
    if user is None:
        await say(update, t("en", "need_start"))
        return
    lang = lang_of(user)
    step = user["step"]

    if step == "blocked":
        await say(update, t(lang, "age_blocked"))
        return
    if step in onboarding.TEXT_STEPS:
        res = onboarding.handle_text(step, text)
        if res.error_key:
            await say(update, t(lang, res.error_key))
            return
        s.db.update_user(tg_id, step=res.next_step, **res.updates)
        user = s.db.get_user(tg_id)
        if res.next_step == "done":
            await finish_onboarding(update, ctx, user)
        else:
            await ask_current_step(update, user)
        return
    if step != "done":
        await ask_current_step(update, user)
        return

    # Безопасность идёт до проверки доступа и лимитов, и не зависит от модели.
    flag = safety.check(text)
    if flag:
        canned = t(lang, flag)
        s.db.add_message(tg_id, "user", text, effective_mode(user))
        s.db.add_message(tg_id, "assistant", canned, effective_mode(user))
        await say(update, canned)
        return

    if not schedule.has_access(user, s.settings, now_utc()):
        await say(update, t(lang, "expired", link=s.settings.payment_link or "-"))
        return
    if s.db.user_messages_since(tg_id, now_utc() - timedelta(hours=24)) >= s.settings.daily_message_limit:
        await say(update, t(lang, "rate_limited"))
        return

    mode = effective_mode(user)
    s.db.add_message(tg_id, "user", text, mode)
    await ctx.bot.send_chat_action(update.effective_chat.id, ChatAction.TYPING)
    try:
        reply = await s.coach.reply(user, text, mode)
    except Exception:
        log.exception("coach.reply failed")
        await say(update, t(lang, "error"))
        return
    s.db.add_message(tg_id, "assistant", reply, mode)
    await say(update, reply)


# ---------- расписание ----------

async def tick(ctx: ContextTypes.DEFAULT_TYPE) -> None:
    """Каждые 15 минут: проверяем, кому пора написать. Отметка ставится ДО отправки,
    поэтому сбой модели означает пропущенный чек-ин, а не бесконечные повторы."""
    s = svc(ctx)
    now = now_utc()
    for user in s.db.all_users():
        for slot in schedule.due_slots(user, s.settings, now):
            try:
                await run_slot(ctx, s, user, slot, now)
            except Exception:
                log.exception("slot %s failed for %s", slot, user["tg_id"])


async def run_slot(ctx, s: Services, user, slot: str, now) -> None:
    tg_id = user["tg_id"]
    local = now.astimezone(ZoneInfo(user["tz"] or s.settings.default_tz))
    if slot in ("morning", "evening"):
        s.db.update_user(tg_id, mode=slot, mode_set_at=iso(now), **{f"last_{slot}_date": local.date().isoformat()})
        text = await s.coach.opener(user, slot)
        s.db.add_message(tg_id, "assistant", text, slot)
    else:
        s.db.update_user(tg_id, last_report_week=schedule.week_key(local))
        prev_start, mid, end = schedule.week_bounds(now)
        total = s.db.drinks_total(tg_id, mid, end)
        prev = s.db.drinks_total(tg_id, prev_start, mid)
        facts = schedule.weekly_facts(total, user["baseline_per_week"], prev)
        text = await s.coach.weekly_report(user, facts)
        s.db.add_message(tg_id, "assistant", text, "general")
    await ctx.bot.send_message(tg_id, text)


async def on_error(update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    log.error("unhandled error", exc_info=ctx.error)


def build_app(settings: Settings, client=None) -> Application:
    db = Database(settings.db_path)
    client = client or anthropic.AsyncAnthropic(api_key=settings.anthropic_api_key)
    app = Application.builder().token(settings.telegram_token).build()
    app.bot_data["svc"] = Services(settings, db, Coach(client, settings, db))
    for name, fn in [("start", cmd_start), ("help", cmd_help), ("sos", cmd_sos), ("log", cmd_log),
                     ("stats", cmd_stats), ("lang", cmd_lang), ("timezone", cmd_timezone),
                     ("delete", cmd_delete), ("grant", cmd_grant)]:
        app.add_handler(CommandHandler(name, fn))
    app.add_handler(CallbackQueryHandler(on_button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))
    app.add_error_handler(on_error)
    app.job_queue.run_repeating(tick, interval=TICK_SECONDS, first=20)
    return app


def main() -> None:
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    logging.getLogger("httpx").setLevel(logging.WARNING)
    build_app(Settings.from_env()).run_polling()
