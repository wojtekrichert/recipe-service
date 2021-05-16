from enum import Enum

from pydantic import BaseSettings


class Settings(BaseSettings):
    class LogLevel(Enum):
        DEBUG = "DEBUG"
        INFO = "INFO"
        WARN = "WARN"
        WARNING = "WARNING"
        ERROR = "ERROR"
        CRITICAL = "CRITICAL"

    APP: str
    DEBUG: bool = False
    ENDPOINT: str
    LOG_LEVEL: LogLevel

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
