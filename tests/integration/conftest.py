import uuid
import pytest

from src.core.database import NoteModel, UserModel
from src.core.repository import AbstractRepository, make_sqlalchemy_repo
from src.core.schemas import Status


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
def get_db_note(**kwargs):
    return NoteModel(
        title='Test',
        author_id=1,
        description='Simple description',
        status=Status.COMPLETED,
        **kwargs
    )
