import asyncio
from datetime import datetime, timedelta, timezone
from types import SimpleNamespace

import pytest

from mira import onboarding, safety, schedule
from mira.coach import Coach, effective_mode, normalize_history
from mira.config import Settings
from mira.db import Database, iso, now_utc


def settings(**kw):
    return Settings(telegram_token="x", anthropic_api_key="y", **kw)


@pytest.fixture
def db():
    return Database(":memory:")


def ready_user(db, tg_id=1, **fields):
    db.create_user(tg_id, "Asia/Jerusalem", 7)
    db.update_user(tg_id, step="done", lang="en", name="Dan", goal="cut_back",
                   baseline_per_week=14, drink="red wine", **fields)
    return db.get_user(tg_id)


# ---- safety ----
@pytest.mark.parametrize("text,expected", [
    ("I want to die", "crisis"),
    ("Хочу умереть", "crisis"),
    ("не хочу жить больше", "crisis"),
    ("my hands are shaking and I had a seizure", "withdrawal"),
    ("у меня судороги", "withdrawal"),
    ("Галлюцинации после того как бросил", "withdrawal"),
    ("I really want a drink tonight", None),
    ("Тяжёлый день, хочется выпить", None),
])
def test_safety(text, expected):
    assert safety.check(text) == expected


# ---- onboarding ----
def test_baseline_parsing():
    assert onboarding.handle_text("baseline", "about 14 a week").updates == {"baseline_per_week": 14}
    assert onboarding.handle_text("baseline", "много").error_key == "q_baseline_bad"
    assert onboarding.handle_text("baseline", "9999").error_key == "q_baseline_bad"


def test_onboarding_chain_reaches_done():
    step, seen = "name", []
    for text in ["Dan", "14", "wine", "evenings", "tried quitting", "sleep"]:
        res = onboarding.handle_text(step, text)
        assert res.error_key is None
        seen.append(step)
        step = res.next_step
        if step == "goal":  # кнопка, не текст
            step = "baseline"
    assert step == "done"


def test_heavy_drinker_flag():
    assert onboarding.is_heavy(40) and not onboarding.is_heavy(14) and not onboarding.is_heavy(None)


# ---- history ----
def test_history_merges_and_starts_with_user():
    rows = [{"role": "assistant", "content": "hi"}, {"role": "user", "content": "a"},
            {"role": "user", "content": "b"}]
    out = normalize_history(rows)
    assert [m["role"] for m in out] == ["user", "assistant", "user"]
    assert out[2]["content"] == "a\nb"


# ---- db ----
def test_delete_user_removes_everything(db):
    u = ready_user(db)
    db.add_message(1, "user", "hi")
    db.log_drink(1, 2, "wine")
    db.start_sos(1)
    db.delete_user(1)
    assert db.get_user(1) is None
    assert db.recent_messages(1) == []
    assert db.drinks_total(1, now_utc() - timedelta(days=1), now_utc() + timedelta(days=1)) == 0


def test_update_user_rejects_unknown_column(db):
    ready_user(db)
    with pytest.raises(ValueError):
        db.update_user(1, created_at="x")


def test_drink_totals_window(db):
    ready_user(db)
    now = now_utc()
    db.log_drink(1, 2, "wine", now - timedelta(days=1))
    db.log_drink(1, 3, "beer", now - timedelta(days=10))
    assert db.drinks_total(1, now - timedelta(days=7), now + timedelta(minutes=1)) == 2


# ---- mode ----
def test_mode_expires(db):
    u = ready_user(db, mode="sos", mode_set_at=iso(now_utc()))
    assert effective_mode(u) == "sos"
    db.update_user(1, mode_set_at=iso(now_utc() - timedelta(hours=4)))
    assert effective_mode(db.get_user(1)) == "general"


# ---- schedule ----
def test_due_slots_morning_evening_and_dedup(db):
    s = settings()
    u = ready_user(db)
    jerusalem_8 = datetime(2026, 10, 7, 5, 30, tzinfo=timezone.utc)  # 08:30 IDT
    assert schedule.due_slots(u, s, jerusalem_8) == ["morning"]
    db.update_user(1, last_morning_date="2026-10-07")
    assert schedule.due_slots(db.get_user(1), s, jerusalem_8) == []
    jerusalem_21 = datetime(2026, 10, 7, 18, 0, tzinfo=timezone.utc)  # 21:00 IDT
    assert schedule.due_slots(db.get_user(1), s, jerusalem_21) == ["evening"]


def test_weekly_report_sunday_evening_once(db):
    s = settings()
    ready_user(db, last_morning_date="2026-10-11", last_evening_date="2026-10-10")
    sunday_21 = datetime(2026, 10, 11, 18, 0, tzinfo=timezone.utc)  # воскресенье 21:00 IDT
    assert set(schedule.due_slots(db.get_user(1), s, sunday_21)) == {"evening", "weekly"}
    db.update_user(1, last_report_week="2026-W41")
    assert "weekly" not in schedule.due_slots(db.get_user(1), s, sunday_21)


def test_no_slots_before_onboarding_done(db):
    db.create_user(5, "Asia/Jerusalem", 7)
    assert schedule.due_slots(db.get_user(5), settings(), now_utc()) == []


def test_paywall(db):
    u = ready_user(db)
    now = now_utc()
    assert schedule.has_access(u, settings(paywall_enabled=False), now + timedelta(days=99))
    paywall = settings(paywall_enabled=True)
    assert schedule.has_access(u, paywall, now)  # триал идёт
    assert not schedule.has_access(u, paywall, now + timedelta(days=8))
    db.update_user(1, paid_until=iso(now + timedelta(days=30)))
    assert schedule.has_access(db.get_user(1), paywall, now + timedelta(days=8))


def test_stats_delta():
    assert schedule.stats_delta(7, 14) == ("delta_less", 50)
    assert schedule.stats_delta(21, 14) == ("delta_more", 50)
    assert schedule.stats_delta(5, None)[0] == "delta_unknown"


# ---- coach с поддельным клиентом ----
class FakeClient:
    def __init__(self):
        self.calls = []
        self.messages = self

    async def create(self, **kw):
        self.calls.append(kw)
        return SimpleNamespace(content=[SimpleNamespace(type="text", text="Hey Dan. What's going on?")])


def test_coach_routes_models_and_builds_context(db):
    u = ready_user(db)
    db.add_message(1, "user", "I want a drink")
    client = FakeClient()
    s = settings(model_chat="chat-model", model_sos="sos-model")
    coach = Coach(client, s, db)

    out = asyncio.run(coach.reply(u, "I want a drink", "sos"))
    assert out.startswith("Hey Dan")
    call = client.calls[-1]
    assert call["model"] == "sos-model"
    assert call["messages"][-1]["role"] == "user"
    assert "Name: Dan" in call["system"][1]["text"] and "SOS" in call["system"][1]["text"]
    assert call["system"][0]["cache_control"] == {"type": "ephemeral"}

    asyncio.run(coach.reply(u, "I want a drink", "general"))
    assert client.calls[-1]["model"] == "chat-model"


def test_opener_appends_instruction_and_handles_empty_history(db):
    u = ready_user(db)
    client = FakeClient()
    coach = Coach(client, settings(), db)
    asyncio.run(coach.opener(u, "morning"))
    msgs = client.calls[-1]["messages"]
    assert msgs[-1]["role"] == "user" and "morning check-in" in msgs[-1]["content"]
