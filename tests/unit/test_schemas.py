import datetime

from src.auth.schemas import User
from src.notes.schemas import Note, Status


def make_user(**kwargs):
    return User(username='Antony', **kwargs)


def make_note(**kwargs):
    return Note(title='10 Push ups', author_id=1, **kwargs)


def test_note_data_is_correct():
    note = make_note(status=Status.COMPLETED)
    assert note.status == Status.COMPLETED
    assert note.__str__() == '[COMPLETED]:10 Push ups'
    assert note.created_at.day == datetime.datetime.today().day


def test_user_data_is_correct():
    user = make_user(email='user@gmail.com')
    assert user.__str__() == 'username=Antony email=user@gmail.com'


def test_notes_are_not_equal():
    note_1 = make_note()
    note_2 = make_note()
    assert note_1 != note_2
