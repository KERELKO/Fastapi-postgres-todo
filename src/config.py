from typing import Any
from pydantic_settings import BaseSettings

from src.constants import Environment, DESCRIPTION


class Config(BaseSettings):
    DATABASE_URL: str = 'sqlite+aiosqlite:///db.sqlite3'
    ENV: Environment = Environment.LOCAL
    LOG_LEVEL: str = 'INFO'
    DOMAIN: str = 'http://127.0.0.1:8000'


settings = Config()

app_configs: dict[str, Any] = {
    'title': 'FastAPI todo app API',
    'description': DESCRIPTION,
}

if not settings.ENV.is_debug:
    app_configs['openapi_url'] = None  # hide docs
