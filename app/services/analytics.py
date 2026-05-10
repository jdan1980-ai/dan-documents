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


# ---------- Forecast: earnings, milestones, grade, velocity (Social Blade-style) ----------


def estimate_earnings(monthly_views: int) -> dict[str, Any]:
    """Rough earnings estimate per month from view count.

    YouTube CPM ranges by niche/region. We use $0.5 (low), $2 (avg), $5 (high)
    per 1000 views. After YouTube's 45% cut, creator gets 55%.
    """
    creator_share = 0.55
    low = monthly_views / 1000 * 0.5 * creator_share
    avg = monthly_views / 1000 * 2.0 * creator_share
    high = monthly_views / 1000 * 5.0 * creator_share
    return {
        "monthly_views": monthly_views,
        "low_usd": round(low, 2),
        "avg_usd": round(avg, 2),
        "high_usd": round(high, 2),
        "yearly_low": round(low * 12, 2),
        "yearly_avg": round(avg * 12, 2),
        "yearly_high": round(high * 12, 2),
    }


def project_milestones(channel: dict[str, Any], videos: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Project when channel hits next subscriber milestones."""
    subs = channel.get("subscribers") or 0
    if not subs or len(videos) < 3:
        return []

    dates = sorted([_parse_dt(v.get("published_at")) for v in videos if _parse_dt(v.get("published_at"))])
    if len(dates) < 2:
        return []

    span_days = max(1, (dates[-1] - dates[0]).days)
    sub_growth_per_day = subs / max(span_days, 1) * 0.5

    if sub_growth_per_day <= 0:
        return []

    targets = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
    out = []
    today = datetime.now(timezone.utc)
    for t in targets:
        if t <= subs:
            continue
        gap = t - subs
        days = int(gap / sub_growth_per_day)
        if days > 365 * 10:
            break
        eta = today.date().fromordinal(today.toordinal() + days)
        out.append({
            "target": t,
            "label": f"{t:,}",
            "days_to": days,
            "eta": eta.isoformat(),
        })
    return out[:6]


_GRADE_THRESHOLDS = [
    (95, "A++"), (90, "A+"), (85, "A"), (80, "A-"),
    (75, "B+"), (70, "B"), (65, "B-"),
    (60, "C+"), (55, "C"), (50, "C-"),
    (40, "D"), (0, "F"),
]


def channel_grade(channel: dict[str, Any], videos: list[dict[str, Any]], summary: dict[str, Any]) -> dict[str, Any]:
    """Channel letter grade based on consistency, engagement, growth velocity."""
    if not videos:
        return {"grade": "F", "score": 0, "reasons": ["Нет видео"]}

    score = 0
    reasons: list[str] = []

    freq = summary.get("upload_frequency_per_week", 0)
    if freq >= 4:
        score += 30; reasons.append(f"Загрузки {freq}/нед — отлично")
    elif freq >= 2:
        score += 22; reasons.append(f"Загрузки {freq}/нед — хорошо")
    elif freq >= 1:
        score += 14; reasons.append(f"Загрузки {freq}/нед — слабо")
    elif freq > 0:
        score += 5; reasons.append(f"Загрузки {freq}/нед — критично мало")

    eng = summary.get("engagement_rate", 0)
    if eng >= 5:
        score += 25; reasons.append(f"Engagement {eng}% — топ")
    elif eng >= 3:
        score += 20; reasons.append(f"Engagement {eng}% — хорошо")
    elif eng >= 1.5:
        score += 12; reasons.append(f"Engagement {eng}% — средне")
    else:
        score += 5; reasons.append(f"Engagement {eng}% — низкий")

    subs = channel.get("subscribers") or 0
    med_views = summary.get("median_views", 0)
    if subs > 0:
        ratio = med_views / subs
        if ratio >= 0.3:
            score += 25; reasons.append(f"Активность {ratio:.0%} от subs — топ")
        elif ratio >= 0.15:
            score += 18
        elif ratio >= 0.05:
            score += 10
        else:
            score += 3; reasons.append(f"Активность {ratio:.0%} от subs — низкая")

    if len(videos) >= 10:
        recent_views = [v["views"] for v in videos[:5]]
        old_views = [v["views"] for v in videos[-5:]]
        recent_med = median(recent_views)
        old_med = median(old_views) or 1
        delta = (recent_med - old_med) / old_med
        if delta >= 0.5:
            score += 20; reasons.append(f"Свежие видео +{delta:.0%} к старым — рост")
        elif delta >= 0:
            score += 12
        elif delta >= -0.3:
            score += 5
        else:
            reasons.append(f"Свежие видео {delta:.0%} к старым — падение")

    score = min(100, score)
    grade = next((g for thresh, g in _GRADE_THRESHOLDS if score >= thresh), "F")
    return {"grade": grade, "score": score, "reasons": reasons}


def channel_velocity(videos: list[dict[str, Any]]) -> dict[str, Any]:
    """Categorize channel as Cooling / Stable / Hot / Breakout."""
    if len(videos) < 6:
        return {"label": "Не определена", "reason": "Меньше 6 видео"}

    sorted_by_date = sorted(videos, key=lambda v: v.get("published_at") or "", reverse=True)
    recent = sorted_by_date[:5]
    older = sorted_by_date[5:10] if len(sorted_by_date) >= 10 else sorted_by_date[5:]
    if not older:
        return {"label": "Не определена", "reason": "Мало истории"}

    rec_med = median(v["views"] for v in recent)
    old_med = median(v["views"] for v in older) or 1
    ratio = rec_med / old_med
    if ratio >= 2.0:
        return {"label": "🚀 Breakout", "reason": f"Свежие видео ×{ratio:.1f} от прошлых"}
    if ratio >= 1.3:
        return {"label": "🔥 Hot", "reason": f"Свежие +{(ratio-1)*100:.0f}% к прошлым"}
    if ratio >= 0.85:
        return {"label": "📊 Stable", "reason": f"Свежие на уровне прошлых ({(ratio-1)*100:+.0f}%)"}
    if ratio >= 0.6:
        return {"label": "❄️ Cooling", "reason": f"Свежие {(ratio-1)*100:.0f}% к прошлым"}
    return {"label": "🥶 Frozen", "reason": f"Свежие {(ratio-1)*100:.0f}% к прошлым — серьёзный спад"}


# ---------- Video velocity (vidIQ Vision-style) ----------


def video_velocity(video: dict[str, Any], channel_videos: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    """Calculate views per hour / day for a video and project 30 days."""
    pub = _parse_dt(video.get("published_at"))
    if not pub:
        return {"error": "Нет даты публикации"}

    now = datetime.now(timezone.utc)
    age_h = max((now - pub).total_seconds() / 3600, 1)
    age_d = age_h / 24
    views = video.get("views", 0) or 0

    vph = views / age_h
    vpd = views / age_d

    proj_30d = int(views + vpd * (30 - age_d)) if age_d < 30 else views

    channel_med_vph = None
    channel_compare = None
    if channel_videos and len(channel_videos) >= 5:
        other = [v for v in channel_videos if v["id"] != video["id"]]
        per_h = []
        for v in other:
            p = _parse_dt(v.get("published_at"))
            if not p:
                continue
            ah = max((now - p).total_seconds() / 3600, 1)
            per_h.append(v["views"] / ah)
        if per_h:
            channel_med_vph = median(per_h)
            channel_compare = round(vph / max(channel_med_vph, 0.01), 2)

    return {
        "age_hours": round(age_h, 1),
        "age_days": round(age_d, 1),
        "views": views,
        "views_per_hour": round(vph, 2),
        "views_per_day": int(vpd),
        "projected_30d": proj_30d,
        "channel_median_vph": round(channel_med_vph, 2) if channel_med_vph else None,
        "vs_channel_median": channel_compare,
    }


# ---------- Competitor score (TubeBuddy-style gap analysis) ----------


def competitor_gaps(my_video: dict[str, Any], competitors: list[dict[str, Any]]) -> dict[str, Any]:
    """Compare my video against top-N competitor videos. Surface gaps."""
    if not competitors:
        return {"error": "Нет конкурентов для сравнения"}

    def avg(field, transform=lambda v: v):
        vals = [transform(c.get(field) or 0) for c in competitors]
        return sum(vals) / max(len(vals), 1)

    def avg_len(field):
        vals = [len(c.get(field) or "") for c in competitors]
        return sum(vals) / max(len(vals), 1)

    def avg_count(field):
        vals = [len(c.get(field) or []) for c in competitors]
        return sum(vals) / max(len(vals), 1)

    my_title_len = len(my_video.get("title") or "")
    comp_title_len = avg_len("title")
    my_desc_len = len(my_video.get("description") or "")
    comp_desc_len = avg_len("description")
    my_tags = len(my_video.get("tags") or [])
    comp_tags = avg_count("tags")
    my_duration = my_video.get("duration_s") or 0
    comp_duration = avg("duration_s")

    import re as _re
    def hashtag_count(d):
        return len(_re.findall(r"#\w+", d or ""))
    def timestamp_count(d):
        return len(_re.findall(r"\b\d{1,2}:\d{2}(?::\d{2})?\b", d or ""))

    my_hashtags = hashtag_count(my_video.get("description"))
    comp_hashtags = sum(hashtag_count(c.get("description")) for c in competitors) / max(len(competitors), 1)
    my_timestamps = timestamp_count(my_video.get("description"))
    comp_timestamps = sum(timestamp_count(c.get("description")) for c in competitors) / max(len(competitors), 1)

    gaps: list[dict[str, Any]] = []
    def gap(name, mine, theirs, units=""):
        if theirs == 0 and mine == 0:
            return
        diff_pct = (mine - theirs) / max(abs(theirs), 1) * 100
        status = "✅ ок" if -25 <= diff_pct <= 25 else ("⚠️ меньше" if mine < theirs else "💪 больше")
        gaps.append({
            "name": name,
            "mine": round(mine, 1) if isinstance(mine, float) else mine,
            "theirs": round(theirs, 1),
            "diff_pct": round(diff_pct, 1),
            "status": status,
            "units": units,
        })

    gap("Длина title", my_title_len, comp_title_len, "симв.")
    gap("Длина description", my_desc_len, comp_desc_len, "симв.")
    gap("Кол-во тегов", my_tags, comp_tags, "")
    gap("Длительность", my_duration, comp_duration, "сек")
    gap("Хэштегов в desc", my_hashtags, comp_hashtags, "")
    gap("Таймкодов в desc", my_timestamps, comp_timestamps, "")

    total_views = sum(c.get("views", 0) for c in competitors)
    avg_views = total_views // max(len(competitors), 1)
    my_views = my_video.get("views", 0)
    views_pct = round(my_views / max(avg_views, 1) * 100, 1)

    return {
        "competitors_count": len(competitors),
        "my_views": my_views,
        "competitor_avg_views": avg_views,
        "views_vs_competitors_pct": views_pct,
        "gaps": gaps,
    }


# ---------- Snapshot reader (LiveDune-style history) ----------


def snapshot_delta(latest_snapshot: dict[str, list[dict]] | None, current_videos: list[dict[str, Any]], channel_key: str | None = None) -> dict[str, Any]:
    """Compare current state to latest snapshot. Returns deltas per video and totals."""
    if not latest_snapshot or not current_videos:
        return {"available": False, "reason": "Нет снапшота или видео"}

    channel_data = None
    if channel_key and channel_key in latest_snapshot:
        channel_data = latest_snapshot[channel_key]
    else:
        for k, v in latest_snapshot.items():
            channel_data = v
            break

    if not channel_data:
        return {"available": False, "reason": "Не нашёл канал в снапшоте"}

    snap_by_id = {v["id"]: v for v in channel_data}
    cur_by_id = {v["id"]: v for v in current_videos}
    common = set(snap_by_id.keys()) & set(cur_by_id.keys())

    if not common:
        return {"available": False, "reason": "Нет общих видео между снапшотом и текущим состоянием"}

    deltas = []
    total_delta_views = 0
    for vid in common:
        s = snap_by_id[vid]
        c = cur_by_id[vid]
        d_views = c.get("views", 0) - s.get("views", 0)
        total_delta_views += d_views
        deltas.append({
            "id": vid,
            "title": c.get("title"),
            "snap_views": s.get("views", 0),
            "now_views": c.get("views", 0),
            "delta": d_views,
        })

    deltas.sort(key=lambda x: x["delta"], reverse=True)
    new_videos = [v for v in current_videos if v["id"] not in snap_by_id]

    return {
        "available": True,
        "common_count": len(common),
        "new_videos_count": len(new_videos),
        "total_delta_views": total_delta_views,
        "top_growers": deltas[:10],
        "new_videos": new_videos[:5],
    }


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
