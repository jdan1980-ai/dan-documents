from statistics import median
from typing import Optional

from fastapi import APIRouter, Form, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from ..config import PROJECT_ROOT
from ..presets import PRESETS
from ..services import analytics, transcripts, youtube, ytdlp


router = APIRouter()
templates = Jinja2Templates(directory=PROJECT_ROOT / "templates")


def _video_url(video_id: str) -> str:
    return f"https://youtube.com/watch?v={video_id}"


@router.post("/channel/analyze", response_class=HTMLResponse)
def analyze_channel(
    request: Request,
    query: str = Form(...),
    limit: int = Form(50),
):
    query = query.strip()
    if not query:
        raise HTTPException(status_code=400, detail="query is empty")

    try:
        channel_id = youtube.resolve_channel(query)
    except youtube.YouTubeAPIError as e:
        return templates.TemplateResponse(
            "partials/error.html",
            {"request": request, "error": str(e)},
            status_code=400,
        )

    if not channel_id:
        return templates.TemplateResponse(
            "partials/error.html",
            {"request": request, "error": f"Канал не найден: {query}"},
            status_code=404,
        )

    try:
        channel = youtube.get_channel(channel_id)
        if not channel or not channel.get("uploads_playlist"):
            raise HTTPException(status_code=404, detail="channel has no uploads")

        video_ids = youtube.list_channel_video_ids(channel["uploads_playlist"], limit=limit)
        videos = youtube.get_videos(video_ids)
    except youtube.YouTubeAPIError as e:
        return templates.TemplateResponse(
            "partials/error.html",
            {"request": request, "error": str(e)},
            status_code=400,
        )

    summary = analytics.channel_summary(channel, videos)
    outliers = analytics.detect_outliers(videos)
    series = analytics.time_series(videos)

    top_videos = sorted(videos, key=lambda v: v["views"], reverse=True)[:10]

    return templates.TemplateResponse(
        "partials/channel_report.html",
        {
            "request": request,
            "channel": channel,
            "summary": summary,
            "outliers": outliers[:15],
            "series": series,
            "top_videos": top_videos,
            "video_url": _video_url,
        },
    )


@router.post("/video/analyze", response_class=HTMLResponse)
def analyze_video(
    request: Request,
    query: str = Form(...),
):
    query = query.strip()
    video_id = _extract_video_id(query)
    if not video_id:
        return templates.TemplateResponse(
            "partials/error.html",
            {"request": request, "error": "Не удалось распознать ID видео или ссылку"},
            status_code=400,
        )

    try:
        videos = youtube.get_videos([video_id])
    except youtube.YouTubeAPIError as e:
        return templates.TemplateResponse(
            "partials/error.html",
            {"request": request, "error": str(e)},
            status_code=400,
        )

    if not videos:
        return templates.TemplateResponse(
            "partials/error.html",
            {"request": request, "error": "Видео не найдено"},
            status_code=404,
        )

    video = videos[0]
    title_score = analytics.score_title(video["title"])
    seo = analytics.keyword_density(video["title"], video.get("description", ""), video.get("tags", []))
    age = analytics.age_days(video.get("published_at"))

    transcript = transcripts.get_transcript(video_id)
    keywords = transcripts.top_keywords(transcript["text"]) if transcript else []

    channel_perf: dict = {}
    try:
        channel = youtube.get_channel(video["channel_id"])
        if channel and channel.get("uploads_playlist"):
            ids = youtube.list_channel_video_ids(channel["uploads_playlist"], limit=50)
            channel_videos = youtube.get_videos(ids)
            channel_perf = analytics.video_performance_vs_channel(video, channel_videos)
    except youtube.YouTubeAPIError:
        pass

    return templates.TemplateResponse(
        "partials/video_report.html",
        {
            "request": request,
            "video": video,
            "title_score": title_score,
            "seo": seo,
            "age_days": age,
            "transcript": transcript,
            "keywords": keywords,
            "channel_perf": channel_perf,
            "video_url": _video_url,
        },
    )


@router.post("/keywords/research", response_class=HTMLResponse)
def keyword_research(
    request: Request,
    query: str = Form(...),
    limit: int = Form(20),
):
    query = query.strip()
    if not query:
        raise HTTPException(status_code=400, detail="query is empty")

    try:
        videos = ytdlp.search_no_quota(query, limit=limit)
    except Exception as e:
        return templates.TemplateResponse(
            "partials/error.html",
            {"request": request, "error": f"Поиск не удался: {e}"},
            status_code=500,
        )

    if not videos:
        return templates.TemplateResponse(
            "partials/error.html",
            {"request": request, "error": "Ничего не найдено"},
            status_code=404,
        )

    total_views = sum(v["views"] for v in videos)
    avg_views = total_views // max(len(videos), 1)
    competition = "высокая" if len(videos) >= limit and avg_views > 100_000 else (
        "средняя" if avg_views > 10_000 else "низкая"
    )

    titles_text = " ".join(v["title"] or "" for v in videos)
    related = transcripts.top_keywords(titles_text, top_n=20)
    related = [(kw, n) for kw, n in related if kw.lower() not in query.lower().split()]

    return templates.TemplateResponse(
        "partials/keywords_report.html",
        {
            "request": request,
            "query": query,
            "videos": videos,
            "total_views": total_views,
            "avg_views": avg_views,
            "competition": competition,
            "related": related[:15],
        },
    )


@router.post("/title/score", response_class=HTMLResponse)
def title_score_endpoint(
    request: Request,
    title: str = Form(...),
):
    title = title.strip()
    if not title:
        raise HTTPException(status_code=400, detail="title is empty")
    result = analytics.score_title(title)
    return templates.TemplateResponse(
        "partials/title_score.html",
        {"request": request, "title": title, "result": result},
    )


@router.post("/competitors/breakouts", response_class=HTMLResponse)
def competitor_breakouts(
    request: Request,
    preset: str = Form(""),
    channels: str = Form(""),
    days_window: int = Form(90),
    min_multiplier: float = Form(2.0),
    videos_per_channel: int = Form(50),
):
    """Find recent breakout videos across a cohort of competitor channels."""
    queries: list[str] = []
    if preset and preset in PRESETS:
        queries = [c["id"] for c in PRESETS[preset].get("competitors", [])]
    extra = [line.strip() for line in (channels or "").splitlines() if line.strip()]
    queries.extend(extra)

    if not queries:
        return templates.TemplateResponse(
            "partials/error.html",
            {"request": request, "error": "Укажи preset или хотя бы один канал."},
            status_code=400,
        )

    days_window = max(1, min(365, days_window))
    min_multiplier = max(1.1, min(20.0, min_multiplier))
    videos_per_channel = max(10, min(200, videos_per_channel))

    channels_data: list[dict] = []
    failed: list[str] = []

    for q in queries:
        try:
            channel_id = youtube.resolve_channel(q)
            if not channel_id:
                failed.append(q)
                continue
            ch = youtube.get_channel(channel_id)
            if not ch or not ch.get("uploads_playlist"):
                failed.append(q)
                continue
            video_ids = youtube.list_channel_video_ids(
                ch["uploads_playlist"], limit=videos_per_channel
            )
            videos = youtube.get_videos(video_ids)
            channels_data.append({"channel": ch, "videos": videos})
        except youtube.YouTubeAPIError as e:
            failed.append(f"{q} ({e})")

    if not channels_data:
        return templates.TemplateResponse(
            "partials/error.html",
            {
                "request": request,
                "error": "Ни один канал не удалось загрузить. " + ", ".join(failed[:5]),
            },
            status_code=400,
        )

    breakouts = analytics.find_breakouts(
        channels_data,
        days_window=days_window,
        min_multiplier=min_multiplier,
    )
    summary = analytics.competitor_summary(channels_data)

    per_channel = [
        {
            "channel": e["channel"],
            "median": int(median(v["views"] for v in e["videos"])) if e["videos"] else 0,
            "videos_count": len(e["videos"]),
        }
        for e in channels_data
    ]
    per_channel.sort(key=lambda c: c["median"], reverse=True)

    return templates.TemplateResponse(
        "partials/breakouts_report.html",
        {
            "request": request,
            "breakouts": breakouts[:50],
            "summary": summary,
            "per_channel": per_channel,
            "failed": failed,
            "days_window": days_window,
            "min_multiplier": min_multiplier,
            "video_url": _video_url,
        },
    )


def _extract_video_id(query: str) -> Optional[str]:
    query = query.strip()
    if len(query) == 11 and "/" not in query and " " not in query:
        return query
    if "youtube.com/watch" in query and "v=" in query:
        return query.split("v=", 1)[1].split("&", 1)[0]
    if "youtu.be/" in query:
        return query.split("youtu.be/", 1)[1].split("?", 1)[0].split("/", 1)[0]
    if "youtube.com/shorts/" in query:
        return query.split("/shorts/", 1)[1].split("?", 1)[0].split("/", 1)[0]
    return None
