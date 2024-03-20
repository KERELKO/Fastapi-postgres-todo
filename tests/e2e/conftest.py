import pytest

from src.config import settings

DOMAIN = settings.DOMAIN


@pytest.fixture
def domain():
    return DOMAIN


@pytest.fixture
def dummy_note_dict():
    return {
        "title": "string",
        "author_id": 1,
        "description": "string",
        "status": "UNCOMPLETED",
        "created_at": "2024-03-19T18:32:56.632Z"
    }
