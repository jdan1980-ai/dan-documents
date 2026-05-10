"""YouTube Data API v3 client with SQLite caching to save quota."""
from __future__ import annotations

import logging
from typing import Any, Iterable

import isodate
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from ..config import get_settings
from ..db import cache_get, cache_set


logger = logging.getLogger(__name__)


class YouTubeAPIError(RuntimeError):
    pass


def _client():
    api_key = get_settings().youtube_api_key
    if not api_key or api_key.startswith("AIzaSy_замени"):
        raise YouTubeAPIError(
            "YOUTUBE_API_KEY не задан. Заполни .env по образцу .env.example."
        )
    return build("youtube", "v3", developerKey=api_key, cache_discovery=False)


def _chunked(items: Iterable[str], size: int = 50) -> Iterable[list[str]]:
    buf: list[str] = []
    for item in items:
        buf.append(item)
        if len(buf) >= size:
            yield buf
            buf = []
    if buf:
        yield buf


def get_channel(channel_id: str) -> dict[str, Any] | None:
    cache_key = f"channel:{channel_id}"
    cached = cache_get(cache_key)
    if cached is not None:
        return cached

    try:
        resp = (
            _client()
            .channels()
            .list(
                part="snippet,statistics,contentDetails,brandingSettings",
                id=channel_id,
                maxResults=1,
            )
            .execute()
        )
    except HttpError as e:
        raise YouTubeAPIError(f"Channel fetch failed: {e}") from e

    items = resp.get("items") or []
    if not items:
        return None

    raw = items[0]
    stats = raw.get("statistics", {})
    snippet = raw.get("snippet", {})
    content = raw.get("contentDetails", {})

    result = {
        "id": raw["id"],
        "title": snippet.get("title"),
        "description": snippet.get("description"),
        "country": snippet.get("country"),
        "published_at": snippet.get("publishedAt"),
        "thumbnail": (snippet.get("thumbnails", {}).get("high") or {}).get("url"),
        "subscribers": int(stats.get("subscriberCount", 0)) if stats.get("subscriberCount") else None,
        "views": int(stats.get("viewCount", 0)) if stats.get("viewCount") else None,
        "videos_count": int(stats.get("videoCount", 0)) if stats.get("videoCount") else None,
        "uploads_playlist": (content.get("relatedPlaylists") or {}).get("uploads"),
    }
    cache_set(cache_key, result)
    return result


def resolve_channel(query: str) -> str | None:
    """Resolve a channel handle, URL, or @handle to a channel ID."""
    query = query.strip()
    if query.startswith("UC") and len(query) == 24:
        return query
    if "youtube.com/" in query:
        for marker in ("/channel/",):
            if marker in query:
                return query.split(marker, 1)[1].split("/", 1)[0].split("?", 1)[0]
        for marker in ("/@", "/c/", "/user/"):
            if marker in query:
                handle = query.split(marker, 1)[1].split("/", 1)[0].split("?", 1)[0]
                return _search_channel_id(handle)
    if query.startswith("@"):
        return _search_channel_id(query[1:])
    return _search_channel_id(query)


def _search_channel_id(handle_or_name: str) -> str | None:
    cache_key = f"resolve:{handle_or_name.lower()}"
    cached = cache_get(cache_key)
    if cached is not None:
        return cached or None

    try:
        resp = (
            _client()
            .search()
            .list(
                part="id",
                q=handle_or_name,
                type="channel",
                maxResults=1,
            )
            .execute()
        )
    except HttpError as e:
        raise YouTubeAPIError(f"Channel search failed: {e}") from e

    items = resp.get("items") or []
    if not items:
        cache_set(cache_key, "")
        return None
    channel_id = items[0]["id"]["channelId"]
    cache_set(cache_key, channel_id)
    return channel_id


def list_channel_video_ids(uploads_playlist_id: str, limit: int = 200) -> list[str]:
    cache_key = f"uploads:{uploads_playlist_id}:{limit}"
    cached = cache_get(cache_key)
    if cached is not None:
        return cached

    yt = _client()
    video_ids: list[str] = []
    page_token: str | None = None
    while len(video_ids) < limit:
        try:
            resp = (
                yt.playlistItems()
                .list(
                    part="contentDetails",
                    playlistId=uploads_playlist_id,
                    maxResults=min(50, limit - len(video_ids)),
                    pageToken=page_token,
                )
                .execute()
            )
        except HttpError as e:
            raise YouTubeAPIError(f"Uploads fetch failed: {e}") from e

        for item in resp.get("items", []):
            vid = item.get("contentDetails", {}).get("videoId")
            if vid:
                video_ids.append(vid)
        page_token = resp.get("nextPageToken")
        if not page_token:
            break

    cache_set(cache_key, video_ids)
    return video_ids


def get_videos(video_ids: list[str]) -> list[dict[str, Any]]:
    if not video_ids:
        return []

    results: list[dict[str, Any]] = []
    missing: list[str] = []
    for vid in video_ids:
        cached = cache_get(f"video:{vid}")
        if cached is not None:
            results.append(cached)
        else:
            missing.append(vid)

    yt = _client()
    for batch in _chunked(missing, 50):
        try:
            resp = (
                yt.videos()
                .list(
                    part="snippet,statistics,contentDetails",
                    id=",".join(batch),
                    maxResults=50,
                )
                .execute()
            )
        except HttpError as e:
            raise YouTubeAPIError(f"Videos fetch failed: {e}") from e

        for raw in resp.get("items", []):
            snippet = raw.get("snippet", {})
            stats = raw.get("statistics", {})
            content = raw.get("contentDetails", {})
            duration_iso = content.get("duration", "PT0S")
            try:
                duration_s = int(isodate.parse_duration(duration_iso).total_seconds())
            except Exception:
                duration_s = 0
            video = {
                "id": raw["id"],
                "title": snippet.get("title"),
                "description": snippet.get("description"),
                "channel_id": snippet.get("channelId"),
                "channel_title": snippet.get("channelTitle"),
                "published_at": snippet.get("publishedAt"),
                "tags": snippet.get("tags") or [],
                "category_id": snippet.get("categoryId"),
                "thumbnail": (snippet.get("thumbnails", {}).get("high") or {}).get("url"),
                "duration_s": duration_s,
                "views": int(stats.get("viewCount", 0)) if stats.get("viewCount") else 0,
                "likes": int(stats.get("likeCount", 0)) if stats.get("likeCount") else 0,
                "comments": int(stats.get("commentCount", 0)) if stats.get("commentCount") else 0,
            }
            cache_set(f"video:{video['id']}", video)
            results.append(video)

    by_id = {v["id"]: v for v in results}
    return [by_id[vid] for vid in video_ids if vid in by_id]


def search_videos(query: str, max_results: int = 25) -> list[dict[str, Any]]:
    cache_key = f"search:{query}:{max_results}"
    cached = cache_get(cache_key)
    if cached is not None:
        return cached

    try:
        resp = (
            _client()
            .search()
            .list(
                part="id",
                q=query,
                type="video",
                maxResults=max_results,
                order="relevance",
            )
            .execute()
        )
    except HttpError as e:
        raise YouTubeAPIError(f"Search failed: {e}") from e

    video_ids = [item["id"]["videoId"] for item in resp.get("items", []) if item["id"].get("videoId")]
    videos = get_videos(video_ids)
    cache_set(cache_key, videos)
    return videos


def search_recent_videos(query: str, days: int = 30, max_results: int = 50) -> list[dict[str, Any]]:
    """Search videos published in the last N days, ordered by view count.

    Cost: 100 units per call (search.list). Cached 24h.
    """
    from datetime import datetime, timedelta, timezone
    published_after = (datetime.now(timezone.utc) - timedelta(days=days)).isoformat()
    cache_key = f"search_recent:{query}:{days}:{max_results}"
    cached = cache_get(cache_key)
    if cached is not None:
        return cached

    try:
        resp = (
            _client()
            .search()
            .list(
                part="id",
                q=query,
                type="video",
                maxResults=min(max_results, 50),
                order="viewCount",
                publishedAfter=published_after,
            )
            .execute()
        )
    except HttpError as e:
        raise YouTubeAPIError(f"Recent search failed: {e}") from e

    video_ids = [item["id"]["videoId"] for item in resp.get("items", []) if item["id"].get("videoId")]
    videos = get_videos(video_ids)
    cache_set(cache_key, videos)
    return videos


def get_video_comments(video_id: str, max_results: int = 100) -> list[dict[str, Any]]:
    """Fetch top-level comments for a video. Cost: 1 unit per call."""
    cache_key = f"comments:{video_id}:{max_results}"
    cached = cache_get(cache_key)
    if cached is not None:
        return cached

    comments: list[dict[str, Any]] = []
    page_token: str | None = None
    yt = _client()
    while len(comments) < max_results:
        try:
            resp = (
                yt.commentThreads()
                .list(
                    part="snippet",
                    videoId=video_id,
                    maxResults=min(100, max_results - len(comments)),
                    order="relevance",
                    pageToken=page_token,
                )
                .execute()
            )
        except HttpError as e:
            if "commentsDisabled" in str(e) or "disabled comments" in str(e).lower():
                cache_set(cache_key, [])
                return []
            raise YouTubeAPIError(f"Comments fetch failed: {e}") from e

        for item in resp.get("items", []):
            top = item.get("snippet", {}).get("topLevelComment", {}).get("snippet", {})
            if not top:
                continue
            comments.append(
                {
                    "text": top.get("textDisplay", ""),
                    "author": top.get("authorDisplayName", ""),
                    "likes": int(top.get("likeCount", 0) or 0),
                    "published_at": top.get("publishedAt"),
                }
            )
        page_token = resp.get("nextPageToken")
        if not page_token:
            break

    cache_set(cache_key, comments)
    return comments
