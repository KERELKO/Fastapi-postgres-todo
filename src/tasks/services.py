from typing import Any

from src.auth.schemas import UserRead
from src.core.database import TaskModel
from src.core.exceptions import ApplicationException
from src.core.repositories.base import AbstractRepository
from src.core.repositories.sqlalchemy import SQLAlchemyTasksRepository
from src.tasks.exceptions import TaskDoesNotExist
from src.tasks.schemas import TaskCreate, TaskRead


class TaskService:
    def __init__(self, repo: AbstractRepository = SQLAlchemyTasksRepository):
        self.repo = repo()

    async def get_task_by_id(self, task_id: int, user: UserRead) -> TaskRead:
        task_model = await self.repo.get(task_id)
        if not task_model:
            raise TaskDoesNotExist(task_id)
        task_schema = TaskRead.model_validate(task_model)
        await self.raise_if_not_task_owner(task_schema, user)
        return task_schema

    async def create_task(self, task_schema: TaskCreate) -> TaskRead:
        new_task = await self.repo.create(
            TaskModel(**task_schema.model_dump())
        )
        return TaskRead.model_validate(new_task)

    async def get_all_tasks(self, limit: int = None) -> list[TaskRead]:
        tasks_db = await self.repo.get_all(limit)
        return [TaskRead.model_validate(task) for task in tasks_db]

    async def update_task(self, task_id: int, values: Any, user: UserRead):
        task = await self.repo.get(task_id)
        if not task:
            raise TaskDoesNotExist(task_id)
        await self.raise_if_not_task_owner(task, user)
        await self.repo.update(task_id, values)
        return TaskRead.model_validate(task)

    async def delete_task(self, task_id: int, user: UserRead) -> int:
        task = await self.repo.get(task_id)
        if not task:
            raise TaskDoesNotExist(task_id)
        await self.raise_if_not_task_owner(task, user)
        deleted_task_id = await self.repo.delete(task_id)
        return deleted_task_id

    async def filter_tasks(self, filters: dict, limit: int = None) -> list[TaskRead]:
        tasks = await self.repo.filter_by(filters, limit=limit)
        return [TaskRead.model_validate(task) for task in tasks]

    async def raise_if_not_task_owner(self, task: TaskRead, user: UserRead) -> None:
        if task.author_id != user.id:
            raise ApplicationException('User is not owner of the task')
