from src.schemas import CustomBaseModel


from fastapi_users import schemas


class UserRead(CustomBaseModel, schemas.BaseUser[int]):
    username: str


class UserCreate(CustomBaseModel, schemas.BaseUserCreate):
    username: str


class UserUpdate(CustomBaseModel, schemas.BaseUserUpdate):
    username: str
