from typing import Any
from pydantic_settings import BaseSettings

from src.constants import Environment, DESCRIPTION


class Config(BaseSettings):
    DATABASE_URL: str = 'sqlite+aiosqlite:///main.db'
    ENV: Environment = Environment.LOCAL
    LOG_LEVEL: str = 'INFO'


settings = Config()

app_configs: dict[str, Any] = {
    'title': 'FastAPI todo app',
    'description': DESCRIPTION,
}

if not settings.ENV.is_debug:
    app_configs['openapi_url'] = None  # hide docs
