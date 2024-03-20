import datetime
from typing import Optional, List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine

from src.config import settings
from src.schemas import Status


DATABASE_URL = str(settings.DATABASE_URL)
engine = create_async_engine(DATABASE_URL)


class BaseModel(DeclarativeBase):
    pass


class UserModel(BaseModel):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[Optional[str]]
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
