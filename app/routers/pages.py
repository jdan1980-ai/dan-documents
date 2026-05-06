from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from ..config import PROJECT_ROOT


router = APIRouter()
templates = Jinja2Templates(directory=PROJECT_ROOT / "templates")


@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "page": "home"},
    )


@router.get("/channel", response_class=HTMLResponse)
def channel_page(request: Request):
    return templates.TemplateResponse(
        "channel.html",
        {"request": request, "page": "channel"},
    )


@router.get("/video", response_class=HTMLResponse)
def video_page(request: Request):
    return templates.TemplateResponse(
        "video.html",
        {"request": request, "page": "video"},
    )


@router.get("/keywords", response_class=HTMLResponse)
def keywords_page(request: Request):
    return templates.TemplateResponse(
        "keywords.html",
        {"request": request, "page": "keywords"},
    )


@router.get("/title", response_class=HTMLResponse)
def title_scorer_page(request: Request):
    return templates.TemplateResponse(
        "title.html",
        {"request": request, "page": "title"},
    )
