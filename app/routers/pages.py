from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from ..config import PROJECT_ROOT


router = APIRouter()
templates = Jinja2Templates(directory=PROJECT_ROOT / "templates")


def _page(name: str, page_id: str):
    def handler(request: Request):
        return templates.TemplateResponse(name, {"request": request, "page": page_id})
    return handler


@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "page": "home"})


@router.get("/channel", response_class=HTMLResponse)
def channel_page(request: Request):
    return templates.TemplateResponse("channel.html", {"request": request, "page": "channel"})


@router.get("/video", response_class=HTMLResponse)
def video_page(request: Request):
    return templates.TemplateResponse("video.html", {"request": request, "page": "video"})


@router.get("/keywords", response_class=HTMLResponse)
def keywords_page(request: Request):
    return templates.TemplateResponse("keywords.html", {"request": request, "page": "keywords"})


@router.get("/title", response_class=HTMLResponse)
def title_scorer_page(request: Request):
    return templates.TemplateResponse("title.html", {"request": request, "page": "title"})


@router.get("/seo", response_class=HTMLResponse)
def seo_page(request: Request):
    return templates.TemplateResponse("seo.html", {"request": request, "page": "seo"})


@router.get("/title-batch", response_class=HTMLResponse)
def title_batch_page(request: Request):
    return templates.TemplateResponse("title_batch.html", {"request": request, "page": "title_batch"})


@router.get("/tags-suggest", response_class=HTMLResponse)
def tags_suggest_page(request: Request):
    return templates.TemplateResponse("tags_suggest.html", {"request": request, "page": "tags_suggest"})


@router.get("/thumbnail", response_class=HTMLResponse)
def thumbnail_page(request: Request):
    return templates.TemplateResponse("thumbnail.html", {"request": request, "page": "thumbnail"})


@router.get("/breakout", response_class=HTMLResponse)
def breakout_page(request: Request):
    return templates.TemplateResponse("breakout.html", {"request": request, "page": "breakout"})


@router.get("/compare", response_class=HTMLResponse)
def compare_page(request: Request):
    return templates.TemplateResponse("compare.html", {"request": request, "page": "compare"})


@router.get("/trends", response_class=HTMLResponse)
def trends_page(request: Request):
    return templates.TemplateResponse("trends.html", {"request": request, "page": "trends"})


@router.get("/upload-time", response_class=HTMLResponse)
def upload_time_page(request: Request):
    return templates.TemplateResponse("upload_time.html", {"request": request, "page": "upload_time"})


@router.get("/comments", response_class=HTMLResponse)
def comments_page(request: Request):
    return templates.TemplateResponse("comments.html", {"request": request, "page": "comments"})


@router.get("/forecast", response_class=HTMLResponse)
def forecast_page(request: Request):
    return templates.TemplateResponse("forecast.html", {"request": request, "page": "forecast"})


@router.get("/velocity", response_class=HTMLResponse)
def velocity_page(request: Request):
    return templates.TemplateResponse("velocity.html", {"request": request, "page": "velocity"})


@router.get("/history", response_class=HTMLResponse)
def history_page(request: Request):
    return templates.TemplateResponse("history.html", {"request": request, "page": "history"})


@router.get("/competitor-score", response_class=HTMLResponse)
def competitor_score_page(request: Request):
    return templates.TemplateResponse("competitor_score.html", {"request": request, "page": "competitor_score"})
