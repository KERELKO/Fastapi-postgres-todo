from src.tasks.schemas import Status


def test_task_data_is_correct(get_TaskCreate):
    assert get_TaskCreate.status == Status.COMPLETED


def test_user_data_is_correct(get_UserCreate):
    assert get_UserCreate.email == 'user@example.com'
