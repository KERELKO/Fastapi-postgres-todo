from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

from .database import BaseModel, engine


class AbstractRepository(ABC):

    @abstractmethod
    def add(self, model_cls):
        raise NotImplementedError

    @abstractmethod
    def get(self, model_cls, reference):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    def __init__(self, engine) -> None:
        self.async_session = sessionmaker(
            engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    async def add(self, model: BaseModel) -> int:
        async with self.async_session() as session:
            async with session.begin():
                session.add(model)
                await session.commit()
                return model.id

    async def get(self, model_cls: BaseModel, pk: int) -> BaseModel | None:
        async with self.async_session() as session:
            obj = await session.get(model_cls, pk)
            return obj

    async def list(
        self, model_cls: BaseModel, limit: int = None
    ) -> list[BaseModel]:
        async with self.async_session() as session:
            query = select(model_cls)
            if limit:
                query = query.limit(limit)
            query = await session.execute(query)
            objects = query.scalars().all()
            return objects


def make_sqlalchemy_repo(engine=engine):
    return SQLAlchemyRepository(engine)
