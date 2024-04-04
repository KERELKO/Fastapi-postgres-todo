import sqlalchemy as sql

from src.core.database import TaskModel, UserModel, async_session_maker
from src.core.repositories.base import AbstractRepository


class BaseSQLAlchemyRepository:
    def __init__(self, async_session_factory=async_session_maker):
        self.async_session_factory = async_session_factory


class SQLAlchemyTasksRepository(BaseSQLAlchemyRepository, AbstractRepository):
    async def get(self, id: int) -> TaskModel:
        async with self.async_session_factory() as session:
            return await session.get(TaskModel, id)

    async def create(self, task: TaskModel) -> TaskModel:
        '''Returns new task with id'''
        async with self.async_session_factory() as session:
            session.add(task)
            await session.commit()
            return task

    async def get_all(self, limit: int = None) -> list[TaskModel]:
        async with self.async_session_factory() as session:
            tasks = await session.scalars(sql.select(TaskModel).limit(limit))
            return tasks

    async def update(self, task_id, values) -> None:
        async with self.async_session_factory() as session:
            stmt = (sql.update(TaskModel).where(id=task_id).values(**values))
            await session.execute(stmt)
            await session.commit()

    async def delete(self, task_id) -> int:
        '''Returns id of the deleted task'''
        async with self.async_session_factory() as session:
            stmt = sql.delete(TaskModel).where(id=task_id)
            await session.execute(stmt)
            await session.commit()


class SQLAlchemyUsersRepository(BaseSQLAlchemyRepository, AbstractRepository):
    async def get(self, id: int) -> UserModel:
        ...

    async def create(self) -> int:
        '''Returns id of the created user'''
        ...

    async def get_all(self) -> list[UserModel]:
        ...

    async def update(self):
        ...

    async def delete(self):
        ...
