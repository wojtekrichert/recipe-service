"""Object representation of settings stored in .env file."""
from enum import Enum

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Object representation of settings stored in .env file."""

    class LogLevel(Enum):
        """Log level available in application."""

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
        """General pydantic configuration class."""

        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
