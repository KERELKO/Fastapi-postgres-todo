import pytest


@pytest.mark.asyncio
async def test_add_task_and_get_task(repo, get_db_task):
    new_task = await repo.create(get_db_task)
    assert new_task.id is not None

    task = await repo.get(new_task.id)
    assert task is not None
