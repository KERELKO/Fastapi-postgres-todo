import datetime

import pytest

from src.core.repository import AbstractRepository, make_sqlalchemy_repo
from src.core.database import UserModel, TaskModel

from src.auth.schemas import UserCreate
from src.tasks.schemas import TaskCreate


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
def get_TaskCreate(**kwargs):
    return TaskCreate(
        title='10 Push ups',
        author_id=1,
        completed=True,
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
def get_db_task(**kwargs):
    return TaskModel(
        title='Test',
        author_id=1,
        description='Simple description',
        completed=True,
        created_at=datetime.datetime.now(),
        **kwargs
    )
