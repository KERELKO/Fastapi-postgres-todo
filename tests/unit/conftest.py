import datetime

import pytest

from src.repository import SQLAlchemyRepository
from src.database import engine
from src.schemas import Status


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
