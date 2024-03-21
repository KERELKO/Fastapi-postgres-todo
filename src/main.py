from fastapi import FastAPI
from src.config import app_configs

from src.auth.routes import user_router
from src.auth.routes import router as auth_router
from src.middleware import TimeElapsedMiddleware

from src.notes.routes import router as notes_router


def create_app():
    app = FastAPI(**app_configs)
    app.include_router(auth_router)
    app.include_router(user_router)
    app.add_middleware(middleware_class=TimeElapsedMiddleware)
    app.include_router(notes_router)
    return app
