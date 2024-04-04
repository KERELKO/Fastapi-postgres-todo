import uuid
import pytest

from src.core.database import TaskModel, UserModel
from src.core.repositories.sqlalchemy import make_sqlalchemy_repo
from src.core.repositories.base import AbstractRepository


@pytest.fixture
def repo(repository: AbstractRepository = make_sqlalchemy_repo):
    return repository()


@pytest.fixture
def get_db_user(**kwargs):
    return UserModel(
        username=str(lambda: uuid.uuid4()),
        email=str(lambda: uuid.uuid4()) + '@example.com',
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
        **kwargs
    )
