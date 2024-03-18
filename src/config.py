from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite:///./test.db"
    debug: bool = True
    log_level: str = "INFO"
    secret_key: str = "mysecretkey"

    class Config:
        env_file = ".env"
