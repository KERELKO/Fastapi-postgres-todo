import datetime

import pytest

from src.core.repository import SQLAlchemyRepository
from src.core.database import engine
from src.core.schemas import Status

from src.auth.schemas import UserCreate
from src.notes.schemas import NoteCreate


@pytest.fixture
def repo():
    return SQLAlchemyRepository(engine)


@pytest.fixture
def note_data():
    return {
        'title': 'Test',
        'author_id': 1,
        'description': 'Simple description',
        'status': Status.COMPLETED,
        'created_at': datetime.datetime.now(),
    }


def make_user(**kwargs):
    return UserCreate(username='user1', **kwargs)


def make_note(**kwargs):
    return NoteCreate(title='10 Push ups', author_id=1, **kwargs)
