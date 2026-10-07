"""Какие проактивные сообщения пора отправить пользователю. Чистая логика без Telegram."""

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from .config import Settings
from .db import parse_iso

WINDOW_HOURS = 3  # если бот был выключен, наверстываем в течение окна


def has_access(user, settings: Settings, now: datetime) -> bool:
    if not settings.paywall_enabled:
        return True
    for col in ("trial_ends_at", "paid_until"):
        until = parse_iso(user[col])
        if until and until > now:
            return True
    return False


def due_slots(user, settings: Settings, now_utc_dt: datetime) -> list[str]:
    """Возвращает подмножество ['morning', 'evening', 'weekly']."""
    if user["step"] != "done" or not has_access(user, settings, now_utc_dt):
        return []
    try:
        local = now_utc_dt.astimezone(ZoneInfo(user["tz"] or settings.default_tz))
    except Exception:
        local = now_utc_dt.astimezone(ZoneInfo(settings.default_tz))
    today = local.date().isoformat()
    slots: list[str] = []

    def in_window(hour: int) -> bool:
        return hour <= local.hour < hour + WINDOW_HOURS

    if in_window(user["morning_hour"]) and user["last_morning_date"] != today:
        slots.append("morning")
    if in_window(user["evening_hour"]) and user["last_evening_date"] != today:
        slots.append("evening")
    iso_year, iso_week, iso_day = local.isocalendar()
    week_key = f"{iso_year}-W{iso_week:02d}"
    if iso_day == 7 and in_window(user["evening_hour"]) and user["last_report_week"] != week_key:
        slots.append("weekly")
    return slots


def week_key(local: datetime) -> str:
    y, w, _ = local.isocalendar()
    return f"{y}-W{w:02d}"


def weekly_facts(total: float, baseline: int | None, prev_total: float) -> str:
    parts = [f"drinks logged in the last 7 days: {total:g}"]
    parts.append(f"drinks logged in the 7 days before: {prev_total:g}")
    if baseline:
        parts.append(f"typical weekly drinks before starting: {baseline}")
        pct = round((baseline - total) / baseline * 100)
        parts.append(f"change vs typical week: {pct:+d}% (positive means less)")
    return "; ".join(parts)


def stats_delta(total: float, baseline: int | None) -> tuple[str, int]:
    """Возвращает (ключ i18n, процент)."""
    if not baseline:
        return "delta_unknown", 0
    pct = round(abs(baseline - total) / baseline * 100)
    if total < baseline and pct >= 1:
        return "delta_less", pct
    if total > baseline and pct >= 1:
        return "delta_more", pct
    return "delta_same", 0


def week_bounds(now: datetime) -> tuple[datetime, datetime, datetime]:
    return now - timedelta(days=14), now - timedelta(days=7), now
