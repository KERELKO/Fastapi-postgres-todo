import pytest

from src.core.database import UserModel, TaskModel


@pytest.mark.asyncio
async def test_add_user(repo, get_db_user):
    user_id = await repo.add(get_db_user)
    assert isinstance(user_id, int)


@pytest.mark.asyncio
async def test_get_user(repo):
    user = await repo.get(UserModel, 1)
    assert isinstance(user.username, str)


@pytest.mark.asyncio
async def test_add_task_and_get_task(repo, get_db_task):
    task_id = await repo.add(get_db_task)
    assert isinstance(task_id, int)

    task = await repo.get(TaskModel, task_id)
    assert task is not None
