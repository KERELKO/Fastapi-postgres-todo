import datetime

import pytest

from src.core.repository import AbstractRepository, make_sqlalchemy_repo
from src.core.database import UserModel, NoteModel
from src.core.schemas import Status

from src.auth.schemas import UserCreate
from src.notes.schemas import NoteCreate


@pytest.fixture
def repo(repository: AbstractRepository = make_sqlalchemy_repo):
    return repository()


@pytest.fixture
def get_UserCreate(**kwargs):
    return UserCreate(
        username='user1',
        email='user@example.com',
        password='1234',
        is_active=True,
        is_superuser=False,
        is_verified=False,
        **kwargs
    )


@pytest.fixture
def get_NoteCreate(**kwargs):
    return NoteCreate(
        title='10 Push ups',
        author_id=1,
        status='COMPLETED',
        **kwargs
    )


@pytest.fixture
def get_db_user(**kwargs):
    return UserModel(
        username='user1',
        email='user@example.com',
        hashed_password='1234',
        is_active=True,
        is_superuser=False,
        is_verified=False,
        **kwargs
    )


@pytest.fixture
def get_db_note(**kwargs):
    return NoteModel(
        title='Test',
        author_id=1,
        description='Simple description',
        status=Status.COMPLETED,
        created_at=datetime.datetime.now(),
        **kwargs
    )
