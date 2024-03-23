from fastapi import HTTPException
from src.core import database as db
from src.utils.web import raise_404_if_none
from src.core.repository import make_sqlalchemy_repo
from src.tasks.schemas import (
    BaseTaskModel,
    TaskRead,
    BaseTaskOutModel,
)


repo = make_sqlalchemy_repo()


async def get_filtered_tasks(
    filters: dict, limit: int = None, scheme: BaseTaskModel = TaskRead,
) -> list[BaseTaskModel]:
    tasks = await repo.filter_by(db.TaskModel, filters, limit)
    return [scheme(**task.__dict__) for task in tasks]


async def get_task_list(
    limit: int = None, scheme: BaseTaskModel = TaskRead
) -> list[BaseTaskModel]:
    tasks = await repo.get_all(db.TaskModel, limit=limit)
    return [scheme(**task.__dict__) for task in tasks]


async def create_task(
    data: dict, scheme: BaseTaskOutModel = TaskRead
) -> BaseTaskOutModel:
    data_id = await repo.add(db.TaskModel(**data))
    return scheme(**data, id=data_id)


async def get_task(
    task_id: int, user: db.UserModel, scheme: BaseTaskModel = TaskRead
) -> BaseTaskOutModel:
    task = await repo.get(db.TaskModel, task_id)
    await raise_404_if_none(
        task, message=f'Task with id \'{task_id}\' not found'
    )
    if task.author_id != user.id:
        raise HTTPException(403, detail='Permission denied')
    return scheme(**task.__dict__)


async def update_task(
    data: dict, task_id: int, user: db.UserModel, scheme: TaskRead = TaskRead
) -> TaskRead:
    task = await repo.get(db.TaskModel, task_id)
    await raise_404_if_none(
        task, message=f'Task with id \'{task_id}\' not found'
    )
    if task.author_id != user.id:
        raise HTTPException(403, detail='Permission denied')
    updated_task = await repo.update(db.TaskModel, pk=task_id, values=data)
    return scheme(**updated_task.__dict__)


async def delete_task(task_id: int, user: db.UserModel) -> int:
    task = await repo.get(db.TaskModel, task_id)
    await raise_404_if_none(
        task, message=f'Task with id \'{task_id}\' not found'
    )
    if task.author_id != user.id:
        raise HTTPException(403, detail='Permission denied')
    deleted_task_id = await repo.delete(db.TaskModel, pk=task_id)
    return deleted_task_id
