"""Read latest snapshot from data/channels_snapshot.json."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..config import PROJECT_ROOT


SNAPSHOT_FILE = PROJECT_ROOT / "data" / "channels_snapshot.json"


def load_latest() -> dict[str, list[dict[str, Any]]] | None:
    if not SNAPSHOT_FILE.exists():
        return None
    try:
        with open(SNAPSHOT_FILE, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return None


def snapshot_age_seconds() -> int | None:
    if not SNAPSHOT_FILE.exists():
        return None
    import time
    return int(time.time() - SNAPSHOT_FILE.stat().st_mtime)


def find_channel_key(channel_id_or_handle: str, snapshot: dict[str, list[dict]] | None) -> str | None:
    if not snapshot:
        return None
    needle = channel_id_or_handle.lower().lstrip("@")
    for k in snapshot.keys():
        if needle in k.lower():
            return k
    return None
