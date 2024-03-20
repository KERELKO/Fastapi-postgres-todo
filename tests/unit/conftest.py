import datetime

import pytest

from src.repository import SQLAlchemyRepository
from src.database import engine
from src.schemas import Status
from src.auth.schemas import UserCreate
from src.notes.schemas import Note


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
    return Note(title='10 Push ups', author_id=1, **kwargs)
