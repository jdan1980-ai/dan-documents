"""yt-dlp wrappers — fetch metadata without using YouTube API quota."""
from __future__ import annotations

from typing import Any

from yt_dlp import YoutubeDL

from ..db import cache_get, cache_set


_BASE_OPTS = {
    "quiet": True,
    "no_warnings": True,
    "skip_download": True,
    "extract_flat": False,
    "noplaylist": True,
}


def search_no_quota(query: str, limit: int = 20) -> list[dict[str, Any]]:
    """Use yt-dlp's ytsearch to find videos without spending API quota."""
    cache_key = f"ytdlp_search:{query}:{limit}"
    cached = cache_get(cache_key)
    if cached is not None:
        return cached

    opts = {**_BASE_OPTS, "extract_flat": True, "default_search": f"ytsearch{limit}"}
    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(query, download=False)

    entries = info.get("entries") or []
    results = []
    for e in entries:
        if not e:
            continue
        results.append(
            {
                "id": e.get("id"),
                "title": e.get("title"),
                "channel": e.get("channel") or e.get("uploader"),
                "channel_id": e.get("channel_id"),
                "duration_s": int(e.get("duration") or 0),
                "views": int(e.get("view_count") or 0),
                "url": e.get("url") or f"https://youtube.com/watch?v={e.get('id')}",
                "thumbnail": e.get("thumbnail"),
            }
        )
    cache_set(cache_key, results)
    return results


def get_video_meta(video_id: str) -> dict[str, Any] | None:
    cache_key = f"ytdlp_video:{video_id}"
    cached = cache_get(cache_key)
    if cached is not None:
        return cached

    url = f"https://youtube.com/watch?v={video_id}"
    with YoutubeDL(_BASE_OPTS) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
        except Exception:
            return None

    result = {
        "id": info.get("id"),
        "title": info.get("title"),
        "description": info.get("description"),
        "channel": info.get("channel"),
        "channel_id": info.get("channel_id"),
        "tags": info.get("tags") or [],
        "categories": info.get("categories") or [],
        "duration_s": int(info.get("duration") or 0),
        "views": int(info.get("view_count") or 0),
        "likes": int(info.get("like_count") or 0),
        "comments": int(info.get("comment_count") or 0),
        "upload_date": info.get("upload_date"),
        "thumbnail": info.get("thumbnail"),
    }
    cache_set(cache_key, result)
    return result
