"""SQLite-хранилище. Для прототипа хватает с запасом; схема совпадает по смыслу
с таблицами для Supabase, так что миграция потом простая."""

import sqlite3
from datetime import datetime, timedelta, timezone

USER_COLUMNS = {
    "lang", "name", "tz", "step", "mode", "mode_set_at", "goal", "baseline_per_week",
    "drink", "triggers", "tried", "motivation", "trial_ends_at", "paid_until",
    "morning_hour", "evening_hour", "last_morning_date", "last_evening_date",
    "last_report_week",
}

SCHEMA = """
create table if not exists users (
  tg_id integer primary key,
  lang text default 'en',
  name text,
  tz text,
  step text default 'lang',
  mode text default 'general',
  mode_set_at text,
  goal text,
  baseline_per_week integer,
  drink text,
  triggers text,
  tried text,
  motivation text,
  created_at text,
  trial_ends_at text,
  paid_until text,
  morning_hour integer default 8,
  evening_hour integer default 20,
  last_morning_date text,
  last_evening_date text,
  last_report_week text
);
create table if not exists messages (
  id integer primary key autoincrement,
  tg_id integer not null,
  role text not null check (role in ('user','assistant')),
  content text not null,
  mode text,
  created_at text not null
);
create index if not exists messages_user_time on messages(tg_id, id desc);
create table if not exists drinks (
  id integer primary key autoincrement,
  tg_id integer not null,
  logged_at text not null,
  count real not null,
  drink_type text
);
create index if not exists drinks_user_time on drinks(tg_id, logged_at);
create table if not exists sos_sessions (
  id integer primary key autoincrement,
  tg_id integer not null,
  started_at text not null,
  ended_at text,
  outcome text
);
"""


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).isoformat()


def parse_iso(value: str | None) -> datetime | None:
    return datetime.fromisoformat(value) if value else None


class Database:
    def __init__(self, path: str):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(SCHEMA)

    # users
    def get_user(self, tg_id: int) -> sqlite3.Row | None:
        return self.conn.execute("select * from users where tg_id=?", (tg_id,)).fetchone()

    def create_user(self, tg_id: int, tz: str, trial_days: int) -> sqlite3.Row:
        now = now_utc()
        self.conn.execute(
            "insert or ignore into users (tg_id, tz, created_at, trial_ends_at) values (?,?,?,?)",
            (tg_id, tz, iso(now), iso(now + timedelta(days=trial_days))),
        )
        self.conn.commit()
        return self.get_user(tg_id)

    def update_user(self, tg_id: int, **fields) -> None:
        bad = set(fields) - USER_COLUMNS
        if bad:
            raise ValueError(f"unknown user columns: {bad}")
        if not fields:
            return
        sets = ", ".join(f"{k}=?" for k in fields)
        self.conn.execute(f"update users set {sets} where tg_id=?", (*fields.values(), tg_id))
        self.conn.commit()

    def all_users(self) -> list[sqlite3.Row]:
        return self.conn.execute("select * from users").fetchall()

    def delete_user(self, tg_id: int) -> None:
        for table in ("messages", "drinks", "sos_sessions", "users"):
            self.conn.execute(f"delete from {table} where tg_id=?", (tg_id,))
        self.conn.commit()

    # messages
    def add_message(self, tg_id: int, role: str, content: str, mode: str | None = None) -> None:
        self.conn.execute(
            "insert into messages (tg_id, role, content, mode, created_at) values (?,?,?,?,?)",
            (tg_id, role, content, mode, iso(now_utc())),
        )
        self.conn.commit()

    def recent_messages(self, tg_id: int, limit: int = 20) -> list[sqlite3.Row]:
        rows = self.conn.execute(
            "select * from messages where tg_id=? order by id desc limit ?", (tg_id, limit)
        ).fetchall()
        return list(reversed(rows))

    def user_messages_since(self, tg_id: int, since: datetime) -> int:
        return self.conn.execute(
            "select count(*) from messages where tg_id=? and role='user' and created_at>=?",
            (tg_id, iso(since)),
        ).fetchone()[0]

    # drinks
    def log_drink(self, tg_id: int, count: float, drink_type: str | None, when: datetime | None = None) -> None:
        self.conn.execute(
            "insert into drinks (tg_id, logged_at, count, drink_type) values (?,?,?,?)",
            (tg_id, iso(when or now_utc()), count, drink_type),
        )
        self.conn.commit()

    def drinks_total(self, tg_id: int, start: datetime, end: datetime) -> float:
        return self.conn.execute(
            "select coalesce(sum(count),0) from drinks where tg_id=? and logged_at>=? and logged_at<?",
            (tg_id, iso(start), iso(end)),
        ).fetchone()[0]

    # sos
    def start_sos(self, tg_id: int) -> int:
        cur = self.conn.execute(
            "insert into sos_sessions (tg_id, started_at) values (?,?)", (tg_id, iso(now_utc()))
        )
        self.conn.commit()
        return cur.lastrowid

    def end_latest_sos(self, tg_id: int, outcome: str) -> None:
        self.conn.execute(
            "update sos_sessions set ended_at=?, outcome=? where id="
            "(select max(id) from sos_sessions where tg_id=? and ended_at is null)",
            (iso(now_utc()), outcome, tg_id),
        )
        self.conn.commit()
