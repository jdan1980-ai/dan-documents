import logging

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .config import PROJECT_ROOT, get_settings
from .db import init_db
from .routers import api, pages


def create_app() -> FastAPI:
    settings = get_settings()
    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    init_db()

    app = FastAPI(
        title="YouTube Analytics",
        description="vidIQ-style analytics built on YouTube Data API + free sources",
        version="0.1.0",
    )

    app.mount(
        "/static",
        StaticFiles(directory=PROJECT_ROOT / "static"),
        name="static",
    )

    app.include_router(pages.router)
    app.include_router(api.router, prefix="/api")

    return app


app = create_app()
