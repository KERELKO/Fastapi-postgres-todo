from src.schemas import CustomBaseModel


from fastapi_users import schemas


class BaseUser(CustomBaseModel):
    username: str


class UserRead(BaseUser, schemas.BaseUser[int]):
    pass


class UserCreate(BaseUser, schemas.BaseUserCreate):
    pass


class UserUpdate(BaseUser, schemas.BaseUserUpdate):
    pass
