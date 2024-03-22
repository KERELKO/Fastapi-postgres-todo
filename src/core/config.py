import os
from typing import Any

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from .constants import Environment, DESCRIPTION

load_dotenv()


class Config(BaseSettings):
    DATABASE_URL: str = os.getenv('DATABASE_URL')
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
