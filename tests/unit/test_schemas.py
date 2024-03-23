def test_task_data_is_correct(get_TaskCreate):
    assert get_TaskCreate.completed is True


def test_user_data_is_correct(get_UserCreate):
    assert get_UserCreate.email == 'user@example.com'
