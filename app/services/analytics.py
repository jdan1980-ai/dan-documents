"""Channel analytics: outliers, growth, engagement, title/thumbnail scoring."""
from __future__ import annotations

import math
import re
from datetime import datetime, timezone
from statistics import median
from typing import Any


def _parse_dt(s: str | None) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None


def channel_summary(channel: dict[str, Any], videos: list[dict[str, Any]]) -> dict[str, Any]:
    """Compute aggregate stats for a channel."""
    if not videos:
        return {
            "videos_analyzed": 0,
            "median_views": 0,
            "avg_views": 0,
            "engagement_rate": 0.0,
            "upload_frequency_per_week": 0.0,
            "best_video": None,
            "worst_video": None,
        }

    views = [v["views"] for v in videos]
    likes = [v["likes"] for v in videos]
    comments = [v["comments"] for v in videos]

    total_engagement = sum(likes) + sum(comments)
    total_views = sum(views) or 1
    engagement_rate = round(total_engagement / total_views * 100, 2)

    dates = [_parse_dt(v["published_at"]) for v in videos]
    dates = [d for d in dates if d]
    upload_freq = 0.0
    if len(dates) >= 2:
        dates.sort()
        span_days = max(1, (dates[-1] - dates[0]).days)
        upload_freq = round(len(dates) / max(span_days / 7, 1), 2)

    best = max(videos, key=lambda v: v["views"])
    worst = min(videos, key=lambda v: v["views"])

    return {
        "videos_analyzed": len(videos),
        "median_views": int(median(views)),
        "avg_views": int(sum(views) / len(views)),
        "max_views": max(views),
        "min_views": min(views),
        "engagement_rate": engagement_rate,
        "upload_frequency_per_week": upload_freq,
        "best_video": best,
        "worst_video": worst,
    }


def detect_outliers(videos: list[dict[str, Any]], threshold: float = 1.5) -> list[dict[str, Any]]:
    """Find videos that significantly outperformed channel median.

    Returns videos sorted by outlier_score desc, with `outlier_score` and
    `multiplier` fields added. Uses log-scale to dampen extreme values.
    """
    if len(videos) < 5:
        return []

    log_views = [math.log10(max(v["views"], 1)) for v in videos]
    med = median(log_views)
    deviations = [abs(lv - med) for lv in log_views]
    mad = median(deviations) or 1.0

    outliers = []
    for v, lv in zip(videos, log_views):
        score = (lv - med) / (mad * 1.4826)
        if score >= threshold:
            multiplier = round(v["views"] / max(10 ** med, 1), 1)
            outliers.append(
                {
                    **v,
                    "outlier_score": round(score, 2),
                    "multiplier": multiplier,
                }
            )
    return sorted(outliers, key=lambda v: v["outlier_score"], reverse=True)


def time_series(videos: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return videos sorted by date ascending with cumulative metrics."""
    items = []
    for v in videos:
        dt = _parse_dt(v.get("published_at"))
        if not dt:
            continue
        items.append(
            {
                "date": dt.date().isoformat(),
                "title": v["title"],
                "views": v["views"],
                "likes": v["likes"],
                "comments": v["comments"],
            }
        )
    return sorted(items, key=lambda x: x["date"])


# ---------- Title scoring ----------

_CLICKBAIT_RU = ["шок", "невероятн", "секрет", "никто не", "правда о", "разоблач", "взорв"]
_CLICKBAIT_EN = ["shocking", "you won't believe", "secret", "nobody tells", "the truth about"]
_POSITIVE = ["лучший", "топ", "best", "top", "ultimate", "идеальн", "perfect"]
_NUMBERS_RE = re.compile(r"\d+")


def score_title(title: str) -> dict[str, Any]:
    """Heuristic title scoring (0-100)."""
    if not title:
        return {"score": 0, "factors": {}}

    factors: dict[str, Any] = {}
    score = 50

    length = len(title)
    factors["length"] = length
    if 40 <= length <= 70:
        score += 15
    elif length < 25:
        score -= 15
    elif length > 100:
        score -= 10

    has_number = bool(_NUMBERS_RE.search(title))
    factors["has_number"] = has_number
    if has_number:
        score += 8

    upper_ratio = sum(1 for c in title if c.isupper()) / max(length, 1)
    factors["upper_ratio"] = round(upper_ratio, 2)
    if upper_ratio > 0.5:
        score -= 15

    lower = title.lower()
    clickbait = sum(1 for kw in _CLICKBAIT_RU + _CLICKBAIT_EN if kw in lower)
    factors["clickbait_markers"] = clickbait
    if clickbait >= 1:
        score += 5
    if clickbait >= 3:
        score -= 10

    positive = sum(1 for kw in _POSITIVE if kw in lower)
    factors["positive_markers"] = positive
    score += min(positive * 4, 12)

    has_question = "?" in title
    factors["has_question"] = has_question
    if has_question:
        score += 5

    has_brackets = "(" in title or "[" in title
    factors["has_brackets"] = has_brackets
    if has_brackets:
        score += 3

    score = max(0, min(100, score))
    return {"score": score, "factors": factors}


def keyword_density(title: str, description: str, tags: list[str]) -> dict[str, Any]:
    """Find keywords shared between title, description and tags — proxy for SEO."""
    title_words = set(re.findall(r"\w{4,}", (title or "").lower()))
    desc_words = set(re.findall(r"\w{4,}", (description or "").lower()))
    tag_words = set(re.findall(r"\w{4,}", " ".join(tags or []).lower()))

    overlap_title_desc = title_words & desc_words
    overlap_title_tags = title_words & tag_words

    return {
        "title_unique_words": len(title_words),
        "desc_unique_words": len(desc_words),
        "tags_count": len(tags or []),
        "overlap_title_desc": sorted(overlap_title_desc),
        "overlap_title_tags": sorted(overlap_title_tags),
        "seo_consistency": round(
            (len(overlap_title_desc) + len(overlap_title_tags))
            / max(len(title_words), 1)
            * 100,
            1,
        ),
    }


def video_performance_vs_channel(video: dict[str, Any], channel_videos: list[dict[str, Any]]) -> dict[str, Any]:
    """How a single video compares to the rest of the channel."""
    if not channel_videos:
        return {}
    other = [v for v in channel_videos if v["id"] != video["id"]]
    if not other:
        return {}
    med_views = median(v["views"] for v in other)
    med_likes = median(v["likes"] for v in other)
    return {
        "views_vs_median": round(video["views"] / max(med_views, 1), 2),
        "likes_vs_median": round(video["likes"] / max(med_likes, 1), 2),
        "channel_median_views": int(med_views),
    }


def age_days(published_at: str | None) -> int | None:
    dt = _parse_dt(published_at)
    if not dt:
        return None
    return (datetime.now(timezone.utc) - dt).days


def find_breakouts(
    channels_data: list[dict[str, Any]],
    days_window: int = 90,
    min_multiplier: float = 2.0,
    min_views: int = 1000,
) -> list[dict[str, Any]]:
    """Find recent breakout videos across competitor channels.

    A breakout = video published within ``days_window`` whose views are
    >= ``min_multiplier`` × that channel's median (from its analyzed history).
    The output is the replicable-formula list: titles + thumbnails + multiplier.

    ``channels_data`` items: ``{"channel": <channel dict>, "videos": [<video>...]}``.
    """
    now = datetime.now(timezone.utc)
    breakouts: list[dict[str, Any]] = []

    for entry in channels_data:
        ch = entry.get("channel") or {}
        videos = entry.get("videos") or []
        if len(videos) < 5:
            continue
        med = median(v["views"] for v in videos) or 1
        for v in videos:
            dt = _parse_dt(v.get("published_at"))
            if not dt:
                continue
            age = (now - dt).days
            if age < 0 or age > days_window:
                continue
            if v["views"] < min_views:
                continue
            multiplier = v["views"] / med
            if multiplier < min_multiplier:
                continue
            breakouts.append(
                {
                    **v,
                    "channel_id": ch.get("id"),
                    "channel_title": ch.get("title"),
                    "channel_subs": ch.get("subscribers"),
                    "channel_median_views": int(med),
                    "multiplier": round(multiplier, 1),
                    "age_days": age,
                }
            )

    return sorted(breakouts, key=lambda b: b["multiplier"], reverse=True)


def competitor_summary(channels_data: list[dict[str, Any]]) -> dict[str, Any]:
    """Aggregate stats across a competitor cohort — useful for benchmarking."""
    total_channels = len(channels_data)
    total_videos = sum(len(e.get("videos") or []) for e in channels_data)
    medians = [
        median(v["views"] for v in e["videos"])
        for e in channels_data
        if e.get("videos")
    ]
    cohort_median = int(median(medians)) if medians else 0
    return {
        "total_channels": total_channels,
        "total_videos": total_videos,
        "cohort_median_views": cohort_median,
    }
