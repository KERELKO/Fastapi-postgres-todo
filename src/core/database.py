import datetime
from typing import AsyncGenerator, List

from fastapi import Depends
from fastapi_users_db_sqlalchemy import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)

from src.core.config import settings
from src.core.schemas import Status


DATABASE_URL = str(settings.DATABASE_URL)
engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class BaseModel(DeclarativeBase):
    pass


class UserModel(SQLAlchemyBaseUserTable[int], BaseModel):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    notes: Mapped[List['NoteModel']] = relationship()

    def __repr__(self):
        return f'UserModel(id={self.id} username={self.username} email={self.email})'


class NoteModel(BaseModel):
    __tablename__ = 'notes'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str]
    status: Mapped[Status]
    created_at: Mapped[datetime.datetime]
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    def __repr__(self):
        return (
            f'NoteModel(id={self.id} '
            f'title={self.title} '
            f'description={self.description} '
            f'status={self.status.value} '
            f'created_at={self.created_at})'
        )


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)
        await conn.run_sync(BaseModel.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, UserModel)
