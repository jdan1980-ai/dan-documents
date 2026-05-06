import json
import sqlite3
import time
from contextlib import contextmanager
from typing import Any, Iterator, Optional

from .config import get_settings


SCHEMA = """
CREATE TABLE IF NOT EXISTS cache (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    created_at INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_cache_created_at ON cache(created_at);
"""


def init_db() -> None:
    with connect() as conn:
        conn.executescript(SCHEMA)


@contextmanager
def connect() -> Iterator[sqlite3.Connection]:
    settings = get_settings()
    conn = sqlite3.connect(settings.db_full_path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def cache_get(key: str, ttl: Optional[int] = None) -> Optional[Any]:
    settings = get_settings()
    ttl = ttl if ttl is not None else settings.cache_ttl
    cutoff = int(time.time()) - ttl
    with connect() as conn:
        row = conn.execute(
            "SELECT value FROM cache WHERE key = ? AND created_at >= ?",
            (key, cutoff),
        ).fetchone()
    if row is None:
        return None
    return json.loads(row["value"])


def cache_set(key: str, value: Any) -> None:
    payload = json.dumps(value, ensure_ascii=False, default=str)
    now = int(time.time())
    with connect() as conn:
        conn.execute(
            "INSERT OR REPLACE INTO cache (key, value, created_at) VALUES (?, ?, ?)",
            (key, payload, now),
        )
