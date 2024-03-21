from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
import sqlalchemy

from .database import BaseModel, engine


class AbstractRepository(ABC):

    @abstractmethod
    def add(self, model_cls):
        raise NotImplementedError

    @abstractmethod
    def get(self, model_cls, reference):
        raise NotImplementedError

    @abstractmethod
    def update(self, data, model_cls, reference):
        raise NotImplementedError

    @abstractmethod
    def delete(self, model_cls, reference):
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
            session.add(model)
            await session.commit()
            return model.id

    async def get(
        self, model_cls: BaseModel, pk: int
    ) -> BaseModel | None:
        async with self.async_session() as session:
            obj = await session.get(model_cls, pk)
            return obj

    async def update(
        self, model_cls: BaseModel, pk: int, values: dict
    ) -> BaseModel | None:
        async with self.async_session() as session:
            stmt = (
                sqlalchemy.update(model_cls)
                .where(model_cls.id == pk)
                .values(**values)
                .returning(model_cls)
            )
            updated_obj = await session.execute(stmt)
            updated_obj_scalar = updated_obj.scalar()
            await session.commit()
            return updated_obj_scalar

    async def delete(self, model_cls: BaseModel, pk: int) -> int | None:
        async with self.async_session() as session:
            obj = await self.get(model_cls, pk)
            if not obj:
                return None
            stmt = sqlalchemy.delete(model_cls).where(model_cls.id == pk)
            await session.execute(stmt)
            await session.commit()
            return pk

    async def filter_by(
        self, model_cls: BaseModel, filters: dict, limit: int = None
    ) -> list[BaseModel | None]:
        async with self.async_session() as session:
            stmt = sqlalchemy.select(model_cls)
            for attr, value in filters.items():
                stmt = stmt.where(getattr(model_cls, attr) == value)
            if limit:
                stmt = stmt.limit(limit)
            query = await session.execute(stmt)
            objects = query.scalars().all()
            return objects

    async def get_all(
        self, model_cls: BaseModel, limit: int = None
    ) -> list[BaseModel | None]:
        async with self.async_session() as session:
            query = sqlalchemy.select(model_cls)
            if limit:
                query = query.limit(limit)
            query = await session.execute(query)
            objects = query.scalars().all()
            return objects


def make_sqlalchemy_repo(engine=engine):
    return SQLAlchemyRepository(engine)
