import datetime
from typing import Optional

from pydantic import Field

from src.core.schemas import (
    CustomBaseModel,
    BaseOutModel,
    Status,
)


class BaseNoteModel(CustomBaseModel):
    pass


class BaseNoteOutModel(BaseOutModel,  BaseNoteModel):
    author_id: int


class NoteCreate(BaseNoteModel):
    title: str
    description: Optional[str] = None
    status: Status = Status.UNCOMPLETED
    created_at: Optional[datetime.datetime] = Field(
        default_factory=datetime.datetime.now,
        kw_only=True,
    )

    def __str__(self):
        return f'[{self.status.value}]:{self.title}'


class NoteOut(NoteCreate, BaseNoteOutModel):
    pass


class NoteUpdate(NoteCreate):
    pass
