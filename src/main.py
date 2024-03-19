from fastapi import FastAPI
from src.config import app_configs


def create_app():
    return FastAPI(**app_configs)
