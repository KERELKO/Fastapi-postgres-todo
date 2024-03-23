from src.notes.schemas import Status


def test_note_data_is_correct(get_NoteCreate):
    assert get_NoteCreate.status == Status.COMPLETED


def test_user_data_is_correct(get_UserCreate):
    assert get_UserCreate.email == 'user@example.com'
