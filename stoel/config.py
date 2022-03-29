from functools import lru_cache

from pydantic import BaseSettings, PostgresDsn  # noqa:  TC002


class Settings(BaseSettings):
    database_url: PostgresDsn


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
