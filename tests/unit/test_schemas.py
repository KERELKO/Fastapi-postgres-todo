import datetime

from .conftest import make_note, make_user
from src.notes.schemas import Status


def test_note_data_is_correct():
    note = make_note(status=Status.COMPLETED)
    assert note.status == Status.COMPLETED
    assert note.__str__() == '[COMPLETED]:10 Push ups'
    assert note.created_at.day == datetime.datetime.today().day


def test_user_data_is_correct():
    user = make_user(email='user@gmail.com')
    assert user.email == 'user@gmail.com'
