import logging
from pathlib import Path

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api import ping, uploads
from app.config import get_settings
from app.db import init_db

log = logging.getLogger("uvicorn")


def additional_setup(app: FastAPI) -> FastAPI:
    settings = get_settings()

    # create filestore folder if it does not exist
    Path(settings.filestore_dir).mkdir(parents=True, exist_ok=True)

    # Set all CORS enabled origins
    if settings.backend_cors_origins:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.backend_cors_origins],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    return app


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(uploads.router, prefix="/upload", tags=["uploads"])
    return application


app = additional_setup(create_application())


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
