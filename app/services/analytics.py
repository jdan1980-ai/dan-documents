"""Channel analytics: outliers, growth, engagement, title/desc/tag scoring, upload-time, comment topics."""
from __future__ import annotations

import math
import re
from collections import Counter
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


# ---------- Description scoring ----------


def score_description(description: str, title: str = "") -> dict[str, Any]:
    """Score description (0-100). Length, keyword repeats, hashtags, CTA, timestamps."""
    if not description:
        return {"score": 0, "factors": {"length": 0, "issues": ["Описание пустое"]}}

    factors: dict[str, Any] = {}
    issues: list[str] = []
    tips: list[str] = []
    score = 50

    length = len(description)
    factors["length"] = length
    if length < 250:
        score -= 15
        issues.append(f"Описание слишком короткое ({length} симв.) — минимум 250 для SEO")
    elif 250 <= length <= 1500:
        score += 10
    elif 1500 < length <= 5000:
        score += 15
    else:
        score += 5
        tips.append("Описание ок, но >5000 — пройдёт обрезку в поиске")

    first_125 = description[:125].lower()
    factors["first_125"] = description[:125]

    title_keywords = set(re.findall(r"\w{4,}", (title or "").lower()))
    main_kw = max(title_keywords, key=len) if title_keywords else None
    factors["main_keyword"] = main_kw

    if main_kw:
        kw_in_first_125 = main_kw in first_125
        factors["kw_in_first_125"] = kw_in_first_125
        if kw_in_first_125:
            score += 10
        else:
            issues.append(f"Главного ключевика '{main_kw}' нет в первых 125 символах (превью YouTube)")

        kw_count = description.lower().count(main_kw)
        factors["main_kw_count"] = kw_count
        if 2 <= kw_count <= 4:
            score += 8
        elif kw_count == 1:
            tips.append(f"Ключевик '{main_kw}' встречается 1 раз — добавь ещё 1-2 повторения")
        elif kw_count > 5:
            score -= 5
            issues.append(f"Ключевик '{main_kw}' повторён {kw_count} раз — выглядит как keyword stuffing")

    hashtags = re.findall(r"#\w+", description)
    factors["hashtag_count"] = len(hashtags)
    factors["hashtags"] = hashtags[:20]
    if 3 <= len(hashtags) <= 15:
        score += 8
    elif len(hashtags) > 15:
        tips.append(f"Хэштегов {len(hashtags)} — YouTube берёт только первые 15 в учёт")

    timestamps = re.findall(r"\b\d{1,2}:\d{2}(?::\d{2})?\b", description)
    has_timestamps = len(timestamps) >= 3
    factors["has_timestamps"] = has_timestamps
    factors["timestamp_count"] = len(timestamps)
    if has_timestamps:
        score += 7
    elif length > 800:
        tips.append("Длинное видео без таймкодов — добавь chapters (формат '0:00 - Intro')")

    cta_patterns = ["subscribe", "подписыв", "подпиш", "like", "лайк", "comment", "коммент", "bell", "колоколь"]
    cta_count = sum(1 for p in cta_patterns if p in description.lower())
    factors["cta_markers"] = cta_count
    if cta_count >= 1:
        score += 5

    links = re.findall(r"https?://\S+", description)
    factors["links_count"] = len(links)
    if len(links) > 0:
        score += 3

    line_breaks = description.count("\n")
    factors["paragraphs"] = line_breaks
    if line_breaks >= 5:
        score += 4

    score = max(0, min(100, score))
    factors["issues"] = issues
    factors["tips"] = tips
    return {"score": score, "factors": factors}


# ---------- Tags scoring ----------


def score_tags(tags: list[str], title: str = "") -> dict[str, Any]:
    """Score tags (0-100). Count, char total, balance, duplicates, title coverage."""
    if not tags:
        return {"score": 0, "factors": {"count": 0, "issues": ["Тегов нет"]}}

    factors: dict[str, Any] = {}
    issues: list[str] = []
    tips: list[str] = []
    score = 50

    count = len(tags)
    factors["count"] = count
    if 15 <= count <= 25:
        score += 15
    elif count < 10:
        score -= 10
        issues.append(f"Тегов {count} — рекомендуется 15-25 для широкого охвата")
    elif count > 30:
        score -= 5
        tips.append(f"Тегов {count} — лимит YouTube 500 символов; проверь чтобы не обрезались")

    total_chars = sum(len(t) for t in tags) + max(0, count - 1)
    factors["total_chars"] = total_chars
    if total_chars > 500:
        score -= 15
        issues.append(f"Общая длина тегов {total_chars} симв. > 500 — YouTube обрежет лишние")
    elif 300 <= total_chars <= 480:
        score += 10

    lengths = [len(t) for t in tags]
    factors["avg_length"] = round(sum(lengths) / max(count, 1), 1)
    factors["min_length"] = min(lengths) if lengths else 0
    factors["max_length"] = max(lengths) if lengths else 0

    short = sum(1 for t in tags if len(t) <= 12)
    medium = sum(1 for t in tags if 12 < len(t) <= 25)
    long_tags = sum(1 for t in tags if len(t) > 25)
    factors["short"] = short
    factors["medium"] = medium
    factors["long"] = long_tags

    if short >= 3 and medium >= 5 and long_tags >= 2:
        score += 8
    else:
        tips.append("Микс не сбалансирован: добавь короткие (≤12), средние (13-25) и long-tail (>25) теги")

    lower_tags = [t.lower().strip() for t in tags]
    duplicates = [t for t, c in Counter(lower_tags).items() if c > 1]
    factors["duplicates"] = duplicates
    if duplicates:
        score -= 10
        issues.append(f"Дубликаты: {', '.join(duplicates)}")

    title_keywords = set(re.findall(r"\w{4,}", (title or "").lower()))
    main_kw = max(title_keywords, key=len) if title_keywords else None
    factors["main_keyword"] = main_kw
    if main_kw:
        coverage = sum(1 for t in lower_tags if main_kw in t)
        factors["main_kw_in_tags"] = coverage
        if coverage >= 1:
            score += 7
        else:
            issues.append(f"Главного ключевика '{main_kw}' нет ни в одном теге")

    spaces = sum(1 for t in tags if " " in t)
    factors["multi_word_tags"] = spaces
    if spaces / max(count, 1) >= 0.5:
        score += 5

    score = max(0, min(100, score))
    factors["issues"] = issues
    factors["tips"] = tips
    return {"score": score, "factors": factors}


# ---------- Auto tag suggestion ----------


_STOP_WORDS = {
    "the", "and", "for", "with", "from", "this", "that", "you", "your", "are", "was", "were",
    "have", "has", "but", "not", "all", "can", "will", "into", "out", "more", "what", "how",
    "why", "when", "where", "who", "which", "than", "then", "there", "their", "them",
    "это", "что", "как", "для", "при", "под", "над", "его", "ему", "она", "они",
}


def suggest_tags(outlier_videos: list[dict[str, Any]], top_n: int = 25) -> list[dict[str, Any]]:
    """Mine tags from outlier videos in the niche.

    Returns tags ranked by frequency across outliers, weighted by views.
    """
    if not outlier_videos:
        return []

    tag_counter: Counter = Counter()
    tag_views: dict[str, int] = {}

    for v in outlier_videos:
        views = max(v.get("views", 1), 1)
        for tag in v.get("tags", []) or []:
            t = tag.lower().strip()
            if not t or len(t) < 3 or t in _STOP_WORDS:
                continue
            tag_counter[t] += 1
            tag_views[t] = tag_views.get(t, 0) + views

    items = [
        {
            "tag": t,
            "count": c,
            "total_views": tag_views.get(t, 0),
            "avg_views": tag_views.get(t, 0) // c,
        }
        for t, c in tag_counter.most_common(top_n * 2)
        if c >= 2
    ]

    items.sort(key=lambda x: (x["count"], x["total_views"]), reverse=True)
    return items[:top_n]


# ---------- Best upload time ----------


_DAYS_RU = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]


def best_upload_time(videos: list[dict[str, Any]]) -> dict[str, Any]:
    """Analyze top performers to suggest best day/hour for uploads."""
    if len(videos) < 5:
        return {"error": "Минимум 5 видео для анализа", "videos_analyzed": len(videos)}

    sorted_videos = sorted(videos, key=lambda v: v["views"], reverse=True)
    top = sorted_videos[: max(10, len(videos) // 3)]
    bottom = sorted_videos[-max(5, len(videos) // 3):]

    def aggregate(group: list[dict[str, Any]]) -> dict[str, Any]:
        days: Counter = Counter()
        hours: Counter = Counter()
        day_views: dict[int, list[int]] = {}
        hour_views: dict[int, list[int]] = {}
        for v in group:
            dt = _parse_dt(v.get("published_at"))
            if not dt:
                continue
            dow = dt.weekday()
            hr = dt.hour
            days[dow] += 1
            hours[hr] += 1
            day_views.setdefault(dow, []).append(v["views"])
            hour_views.setdefault(hr, []).append(v["views"])
        return {"days": days, "hours": hours, "day_views": day_views, "hour_views": hour_views}

    top_agg = aggregate(top)
    bottom_agg = aggregate(bottom)

    def score_dim(top_counter: Counter, bottom_counter: Counter, dim_views: dict[int, list[int]]) -> list[dict[str, Any]]:
        keys = set(top_counter.keys()) | set(bottom_counter.keys())
        out = []
        for k in keys:
            t = top_counter.get(k, 0)
            b = bottom_counter.get(k, 0)
            views_list = dim_views.get(k, [])
            avg_v = int(sum(views_list) / len(views_list)) if views_list else 0
            out.append({"key": k, "top_count": t, "bottom_count": b, "score": t - b, "avg_views": avg_v})
        return sorted(out, key=lambda x: (x["score"], x["avg_views"]), reverse=True)

    days_ranked = score_dim(top_agg["days"], bottom_agg["days"], top_agg["day_views"])
    hours_ranked = score_dim(top_agg["hours"], bottom_agg["hours"], top_agg["hour_views"])

    days_named = [
        {**d, "label": _DAYS_RU[d["key"]]}
        for d in days_ranked
    ]
    hours_named = [
        {**h, "label": f"{h['key']:02d}:00"}
        for h in hours_ranked
    ]

    best_day = days_named[0] if days_named else None
    best_hour = hours_named[0] if hours_named else None

    return {
        "videos_analyzed": len(videos),
        "top_count": len(top),
        "best_day": best_day,
        "best_hour": best_hour,
        "days_ranked": days_named[:7],
        "hours_ranked": hours_named[:8],
    }


# ---------- Comment topics ----------


def comment_topics(comments: list[dict[str, Any]], top_n: int = 25) -> dict[str, Any]:
    """Extract top topic words and sentiment hints from comments."""
    if not comments:
        return {"total": 0, "top_words": [], "questions": 0, "positive_hints": 0, "negative_hints": 0}

    text = " ".join((c.get("text") or "") for c in comments).lower()
    words = re.findall(r"[a-zа-яё]{4,}", text)
    counter: Counter = Counter()
    for w in words:
        if w in _STOP_WORDS:
            continue
        counter[w] += 1

    top_words = [{"word": w, "count": c} for w, c in counter.most_common(top_n)]

    questions = sum(1 for c in comments if "?" in (c.get("text") or ""))

    positive_re = re.compile(r"\b(love|amazing|perfect|awesome|great|best|favourite|favorite|beautiful|relaxing|calming|спасибо|круто|класс|шикарн|любл|обожа)\b", re.IGNORECASE)
    negative_re = re.compile(r"\b(hate|bad|boring|terrible|annoying|skip|stop|ужас|плохо|скучн|не нрав)\b", re.IGNORECASE)
    pos = sum(1 for c in comments if positive_re.search(c.get("text") or ""))
    neg = sum(1 for c in comments if negative_re.search(c.get("text") or ""))

    return {
        "total": len(comments),
        "top_words": top_words,
        "questions": questions,
        "positive_hints": pos,
        "negative_hints": neg,
        "sentiment_ratio": round(pos / max(neg, 1), 2),
    }
