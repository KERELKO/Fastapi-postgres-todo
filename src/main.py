from fastapi import FastAPI
from src.config import app_configs

from src.auth.routes import router as auth_router
from src.auth.middleware import TimeElapsedMiddleware


def create_app():
    app = FastAPI(**app_configs)
    app.include_router(auth_router)
    app.add_middleware(middleware_class=TimeElapsedMiddleware)

    return app
