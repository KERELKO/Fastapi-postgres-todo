import datetime
from typing import Optional

from pydantic import Field

from src.schemas import CustomBaseModel, Status


class Note(CustomBaseModel):
    title: str
    author_id: int
    description: Optional[str] = None
    status: Status = Status.UNCOMPLETED
    created_at: Optional[datetime.datetime] = Field(
        default_factory=datetime.datetime.now,
        kw_only=True,
    )

    def __str__(self):
        return f'[{self.status.value}]:{self.title}'
