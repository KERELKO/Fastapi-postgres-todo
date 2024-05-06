from typing import Optional

from src.core.schemas import CustomBaseSchema, BaseOutSchema


class BaseTaskSchema(CustomBaseSchema):
    ...


class TaskCreate(BaseTaskSchema):
    title: str
    author_id: int
    description: Optional[str] = None
    completed: bool = False

    def __str__(self):
        return f'{self.title}, completed: {self.completed}'


class TaskRead(TaskCreate, BaseOutSchema):
    pass


class TaskUpdate(TaskCreate):
    pass


class TaskFilters(BaseTaskSchema):
    title: str | None = None
    completed: bool | None = None
    author_id: int | None = None
    limit: int | None = None
