from src.core.schemas import CustomBaseSchema

from fastapi_users import schemas


class BaseUser(CustomBaseSchema):
    username: str


class UserRead(BaseUser, schemas.BaseUser[int]):
    pass


class UserCreate(BaseUser, schemas.BaseUserCreate):
    pass


class UserUpdate(BaseUser, schemas.BaseUserUpdate):
    pass
