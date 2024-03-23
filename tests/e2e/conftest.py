import pytest

from src.core.config import settings

DOMAIN = settings.DOMAIN


@pytest.fixture
def auth():
    return ('super@example.com', '1234')


@pytest.fixture
def domain():
    return DOMAIN


@pytest.fixture
def task_json():
    return {
        'title': 'string',
        'author_id': 2,
        'description': 'string',
        'status': 'UNCOMPLETED',
        'created_at': '2024-03-19T18:32:56.632Z',
    }


@pytest.fixture
def user_json():
    return {
        "email": "super@user.com",
        "password": "1234",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "super",
    }
