import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from .constants import Environment, DESCRIPTION

load_dotenv()


class Config(BaseSettings):
    # database settings
    POSTGRES: str = 'postgresql+asyncpg'
    POSTGRES_HOST: str = os.getenv('POSTGRES_HOST')
    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_PORT: int = 5432

    # Use sqlite+aiosqlite for developing in local environment
    # DATABASE_URL: str = 'sqlite+aiosqlite:///db.sqlite3'
    DATABASE_URL: str = f'{POSTGRES}://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}'

    # environment
    ENV: Environment = Environment.LOCAL
    LOG_LEVEL: str = 'INFO'
    DOMAIN: str = 'http://127.0.0.1:8000'


settings = Config()

app_configs: dict[str, any] = {
    'title': 'FastAPI todo app API',
    'description': DESCRIPTION,
}

if not settings.ENV.is_debug:
    app_configs['openapi_url'] = None  # hide docs
