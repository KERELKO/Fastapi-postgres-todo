from src.utils.web import raise_404_if_none
from src.repository import make_sqlalchemy_repo
from src.schemas import BaseOutModel
from src import database as db

from .schemas import (
    UserRead,
    UserUpdate,
    UserCreate,
)


repo = make_sqlalchemy_repo()


async def create_user(
    data: UserCreate = UserCreate, scheme: BaseOutModel = UserRead
) -> UserRead:
    data = db.UserModel(**data.__dict__)
    await repo.add(data)
    return scheme(**data.__dict__)


async def get_user_by_id(
    user_id: int, scheme: BaseOutModel = UserRead
) -> BaseOutModel:
    user = await repo.get(db.UserModel, pk=user_id)
    await raise_404_if_none(
        user,
        message=f'User with id \'{user_id}\' does not exist'
    )
    user_scheme = scheme(**user.__dict__)
    return user_scheme


async def get_user_list(
    limit: int = None, scheme: BaseOutModel = UserRead
) -> list[BaseOutModel]:
    users = await repo.list(db.UserModel, limit=limit)
    return [scheme(**user.__dict__) for user in users]


async def update_user(
    user_id: int, data: UserCreate = UserUpdate
) -> UserCreate:
    updated_user = await repo.update(
        db.UserModel,
        pk=user_id,
        values=data.__dict__
    )
    await raise_404_if_none(
        updated_user,
        message=f'User with id \'{user_id}\' does not exist'
    )


async def delete_user(user_id: int) -> int:
    deleted_user_id = await repo.delete(db.UserModel, pk=user_id)
    await raise_404_if_none(
        deleted_user_id,
        message=f'User with id \'{deleted_user_id}\' does not exist'
    )
    return deleted_user_id
