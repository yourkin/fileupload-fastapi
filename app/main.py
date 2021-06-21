import logging
from pathlib import Path

from fastapi import FastAPI

from app.api import ping, uploads
from app.config import get_settings
from app.db import init_db

log = logging.getLogger("uvicorn")


def additional_setup():
    settings = get_settings()

    # create filestore folder if it does not exist
    Path(settings.filestore_dir).mkdir(parents=True, exist_ok=True)


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(uploads.router, prefix="/upload", tags=["uploads"])
    return application


app = create_application()
additional_setup()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
