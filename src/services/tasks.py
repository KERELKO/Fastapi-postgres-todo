from fastapi import HTTPException

from src.core.database import TaskModel
from src.core.repositories.base import AbstractRepository
from src.core.repositories.sqlalchemy import SQLAlchemyTasksRepository
from src.tasks.schemas import TaskCreate, TaskRead
from src.utils.web import raise_404_if_none


class TasksService:
    def __init__(
        self,
        repo: AbstractRepository = SQLAlchemyTasksRepository,
        unit_of_work=None
    ):
        self.repo = repo()
        # not implemented yet
        self.uow = unit_of_work

    async def get_task_by_id(self, task_id, user):
        task_model = await self.repo.get(task_id)
        task_schema = TaskRead(**task_model.__dict__)
        raise_404_if_none(
            task_schema, message=f'Task with id \'{task_id}\' not found'
        )
        await self.raise_if_not_owner(task_schema, user)
        return task_schema

    async def create_task(self, task_schema: TaskCreate) -> TaskRead:
        new_task = await self.repo.create(TaskModel(**task_schema.__dict__))
        return TaskRead(**new_task.__dict__)

    async def get_all_tasks(self, limit: int = None) -> list[TaskRead]:
        tasks_db = await self.repo.get_all(limit)
        return [TaskRead(**task.__dict__) for task in tasks_db]

    async def update_task(self, task_id, values, user):
        task = await self.repo.get(task_id)
        raise_404_if_none(task)
        await self.raise_if_not_task_owner(task, user)
        await self.repo.update(task_id, values)
        return TaskRead(**task.__dict__)

    async def delete_task(self, task_id, user):
        task = await self.repo.get(task_id)
        raise_404_if_none(task)
        await self.raise_if_not_task_owner(task, user)
        deleted_task_id = await self.repo.delete(task_id)
        return deleted_task_id

    async def raise_if_not_task_owner(self, task, user) -> None:
        if task.author_id != user.id or not user.is_superuser:
            raise HTTPException(403, detail='Permission denied')
