from typing import Optional

from fastapi import APIRouter, File, Form, HTTPException, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from ..config import PROJECT_ROOT
from ..services import analytics, thumbnail, transcripts, trends, youtube, ytdlp


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


# ===========================================================
# NEW: SEO Scorecard (title + description + tags pre-publish)
# ===========================================================


@router.post("/seo/analyze", response_class=HTMLResponse)
def seo_analyze(
    request: Request,
    title: str = Form(""),
    description: str = Form(""),
    tags: str = Form(""),
):
    title = title.strip()
    description = description.strip()
    tag_list = [t.strip() for t in tags.split(",") if t.strip()] if tags else []

    title_result = analytics.score_title(title) if title else None
    desc_result = analytics.score_description(description, title) if description else None
    tags_result = analytics.score_tags(tag_list, title) if tag_list else None
    overlap = analytics.keyword_density(title, description, tag_list) if (title or description or tag_list) else None

    parts = [r["score"] for r in [title_result, desc_result, tags_result] if r]
    overall = round(sum(parts) / len(parts)) if parts else 0

    return templates.TemplateResponse(
        "partials/seo_report.html",
        {
            "request": request,
            "title": title,
            "description": description,
            "tags": tag_list,
            "title_result": title_result,
            "desc_result": desc_result,
            "tags_result": tags_result,
            "overlap": overlap,
            "overall": overall,
        },
    )


# ===========================================================
# NEW: Title A/B batch scoring
# ===========================================================


@router.post("/title/batch", response_class=HTMLResponse)
def title_batch(
    request: Request,
    titles: str = Form(...),
):
    lines = [t.strip() for t in titles.splitlines() if t.strip()]
    if not lines:
        raise HTTPException(status_code=400, detail="нет заголовков")

    results = []
    for line in lines[:10]:
        r = analytics.score_title(line)
        results.append({"title": line, "score": r["score"], "factors": r["factors"]})
    results.sort(key=lambda x: x["score"], reverse=True)

    return templates.TemplateResponse(
        "partials/title_batch.html",
        {"request": request, "results": results},
    )


# ===========================================================
# NEW: Auto-tag suggestion (mining outliers in a niche)
# ===========================================================


@router.post("/tags/suggest", response_class=HTMLResponse)
def tags_suggest(
    request: Request,
    query: str = Form(...),
    max_videos: int = Form(50),
):
    query = query.strip()
    if not query:
        raise HTTPException(status_code=400, detail="query empty")

    try:
        videos = youtube.search_videos(query, max_results=min(max_videos, 50))
    except youtube.YouTubeAPIError as e:
        return templates.TemplateResponse(
            "partials/error.html",
            {"request": request, "error": str(e)},
            status_code=400,
        )

    if not videos:
        return templates.TemplateResponse(
            "partials/error.html",
            {"request": request, "error": "Видео не найдено по запросу"},
            status_code=404,
        )

    outliers = analytics.detect_outliers(videos)
    pool = outliers if outliers else sorted(videos, key=lambda v: v["views"], reverse=True)[:10]
    suggested = analytics.suggest_tags(pool, top_n=30)

    return templates.TemplateResponse(
        "partials/tags_suggest.html",
        {
            "request": request,
            "query": query,
            "videos_total": len(videos),
            "outliers_count": len(outliers),
            "pool_size": len(pool),
            "suggested": suggested,
            "video_url": _video_url,
        },
    )


# ===========================================================
# NEW: Thumbnail analyzer (file upload)
# ===========================================================


@router.post("/thumbnail/analyze", response_class=HTMLResponse)
async def thumbnail_analyze(
    request: Request,
    file: UploadFile = File(...),
):
    data = await file.read()
    if not data:
        raise HTTPException(status_code=400, detail="empty file")

    if len(data) > 10 * 1024 * 1024:
        return templates.TemplateResponse(
            "partials/error.html",
            {"request": request, "error": "Файл больше 10 MB — слишком большой даже для анализа"},
            status_code=400,
        )

    result = thumbnail.analyze_thumbnail(data)
    return templates.TemplateResponse(
        "partials/thumbnail_report.html",
        {"request": request, "result": result, "filename": file.filename},
    )


# ===========================================================
# NEW: Breakout videos in a niche (last N days)
# ===========================================================


@router.post("/breakout/search", response_class=HTMLResponse)
def breakout_search(
    request: Request,
    query: str = Form(...),
    days: int = Form(30),
):
    query = query.strip()
    if not query:
        raise HTTPException(status_code=400, detail="query empty")

    try:
        videos = youtube.search_recent_videos(query, days=days, max_results=50)
    except youtube.YouTubeAPIError as e:
        return templates.TemplateResponse(
            "partials/error.html",
            {"request": request, "error": str(e)},
            status_code=400,
        )

    if not videos:
        return templates.TemplateResponse(
            "partials/error.html",
            {"request": request, "error": "Видео не найдены за этот период"},
            status_code=404,
        )

    outliers = analytics.detect_outliers(videos, threshold=1.0)
    top = sorted(videos, key=lambda v: v["views"], reverse=True)[:20]

    return templates.TemplateResponse(
        "partials/breakout_report.html",
        {
            "request": request,
            "query": query,
            "days": days,
            "total": len(videos),
            "outliers": outliers[:15],
            "top": top,
            "video_url": _video_url,
        },
    )


# ===========================================================
# NEW: Channel-vs-Channel side-by-side
# ===========================================================


def _resolve_and_load(query: str, limit: int = 50) -> tuple[dict, list[dict], dict]:
    cid = youtube.resolve_channel(query)
    if not cid:
        return None, [], {}
    ch = youtube.get_channel(cid)
    if not ch or not ch.get("uploads_playlist"):
        return ch, [], {}
    ids = youtube.list_channel_video_ids(ch["uploads_playlist"], limit=limit)
    videos = youtube.get_videos(ids)
    summary = analytics.channel_summary(ch, videos)
    return ch, videos, summary


@router.post("/compare/channels", response_class=HTMLResponse)
def compare_channels(
    request: Request,
    channel_a: str = Form(...),
    channel_b: str = Form(...),
):
    try:
        a_ch, a_vids, a_sum = _resolve_and_load(channel_a)
        b_ch, b_vids, b_sum = _resolve_and_load(channel_b)
    except youtube.YouTubeAPIError as e:
        return templates.TemplateResponse(
            "partials/error.html",
            {"request": request, "error": str(e)},
            status_code=400,
        )

    if not a_ch or not b_ch:
        return templates.TemplateResponse(
            "partials/error.html",
            {"request": request, "error": "Один из каналов не найден"},
            status_code=404,
        )

    return templates.TemplateResponse(
        "partials/compare_report.html",
        {
            "request": request,
            "a": {"channel": a_ch, "summary": a_sum},
            "b": {"channel": b_ch, "summary": b_sum},
            "video_url": _video_url,
        },
    )


# ===========================================================
# NEW: Google Trends
# ===========================================================


@router.post("/trends/lookup", response_class=HTMLResponse)
def trends_lookup(
    request: Request,
    keyword: str = Form(...),
    geo: str = Form(""),
    timeframe: str = Form("today 12-m"),
):
    keyword = keyword.strip()
    if not keyword:
        raise HTTPException(status_code=400, detail="keyword empty")

    result = trends.trends_for_keyword(keyword, geo=geo, timeframe=timeframe)
    return templates.TemplateResponse(
        "partials/trends_report.html",
        {"request": request, "result": result},
    )


# ===========================================================
# NEW: Best upload time (channel-level analysis)
# ===========================================================


@router.post("/upload-time/analyze", response_class=HTMLResponse)
def upload_time_analyze(
    request: Request,
    query: str = Form(...),
    limit: int = Form(50),
):
    query = query.strip()
    try:
        ch, videos, _ = _resolve_and_load(query, limit=limit)
    except youtube.YouTubeAPIError as e:
        return templates.TemplateResponse(
            "partials/error.html",
            {"request": request, "error": str(e)},
            status_code=400,
        )

    if not ch:
        return templates.TemplateResponse(
            "partials/error.html",
            {"request": request, "error": f"Канал не найден: {query}"},
            status_code=404,
        )

    result = analytics.best_upload_time(videos)
    return templates.TemplateResponse(
        "partials/upload_time_report.html",
        {"request": request, "channel": ch, "result": result},
    )


# ===========================================================
# NEW: Comment topics (sentiment + frequency)
# ===========================================================


@router.post("/comments/analyze", response_class=HTMLResponse)
def comments_analyze(
    request: Request,
    query: str = Form(...),
    max_comments: int = Form(100),
):
    video_id = _extract_video_id(query)
    if not video_id:
        return templates.TemplateResponse(
            "partials/error.html",
            {"request": request, "error": "Не распознан ID видео"},
            status_code=400,
        )

    try:
        comments = youtube.get_video_comments(video_id, max_results=min(max_comments, 200))
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

    topics = analytics.comment_topics(comments)

    return templates.TemplateResponse(
        "partials/comments_report.html",
        {
            "request": request,
            "video": videos[0],
            "comments": comments[:30],
            "topics": topics,
        },
    )
