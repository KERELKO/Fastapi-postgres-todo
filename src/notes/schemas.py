import datetime
from typing import Optional
from uuid import uuid4

from pydantic import Field

from src.schemas import CustomBaseModel, Status
from src.auth.schemas import User


class Note(CustomBaseModel):
    oid: str = Field(
        default_factory=lambda: str(uuid4()),
        kw_only=True,
    )
    title: str
    author: User
    description: Optional[str] = None
    status: Status = Status.UNCOMPLETED
    created_at: Optional[datetime.datetime] = Field(
        default_factory=datetime.datetime.now,
        kw_only=True,
    )

    def __str__(self):
        return f'[{self.status.value}]:{self.title}'

    def __hash__(self):
        return hash(self.oid)

    def __eq__(self, other: 'Note'):
        return self.oid == other.oid
