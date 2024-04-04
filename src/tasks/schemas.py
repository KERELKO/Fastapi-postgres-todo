from typing import Optional

from src.core.schemas import (
    CustomBaseSchema,
    BaseOutSchema,
)


class BaseTaskModel(CustomBaseSchema):
    pass


class TaskCreate(BaseTaskModel):
    title: str
    author_id: int
    description: Optional[str] = None
    completed: bool = False

    def __str__(self):
        return f'[{self.completed}]:{self.title}'


class TaskRead(TaskCreate, BaseOutSchema):
    pass


class TaskUpdate(TaskCreate):
    pass
