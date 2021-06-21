import logging
import os
from functools import lru_cache
from typing import List

from pydantic import BaseSettings, PostgresDsn, AnyHttpUrl

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", False)
    database_url: PostgresDsn = os.environ.get("DATABASE_URL")
    filestore_dir: str = os.environ.get("FILESTORE_DIR", "")
    backend_cors_origins: List[AnyHttpUrl] = []


@lru_cache()
def get_settings() -> Settings:
    log.info("Loading config settings from the environment...")
    return Settings()
