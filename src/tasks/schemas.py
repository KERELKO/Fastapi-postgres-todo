from typing import Optional

from src.core.schemas import (
    CustomBaseModel,
    BaseOutModel,
)


class BaseTaskModel(CustomBaseModel):
    pass


class BaseTaskOutModel(BaseOutModel, BaseTaskModel):
    author_id: int


class TaskCreate(BaseTaskModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

    def __str__(self):
        return f'[{self.completed}]:{self.title}'


class TaskRead(TaskCreate, BaseTaskOutModel):
    pass


class TaskUpdate(TaskCreate):
    pass
