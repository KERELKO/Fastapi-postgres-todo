from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from .database import BaseModel


class AbstractRepository(ABC):

    @abstractmethod
    def add(self, model_cls):
        raise NotImplementedError

    @abstractmethod
    def get(self, model_cls, reference):
        raise NotImplementedError


# TODO: make it asynchronous
class SQLAlchemyRepository(AbstractRepository):
    def __init__(self, engine) -> None:
        self.async_session = sessionmaker(
            engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    async def add(self, model_cls: BaseModel) -> None:
        async with self.async_session() as session:
            async with session.begin():
                session.add(model_cls)
                await session.commit()

    async def get(self, model_cls: BaseModel, pk: int) -> BaseModel:
        async with self.async_session() as session:
            result = await session.get(model_cls, pk)
            return result
