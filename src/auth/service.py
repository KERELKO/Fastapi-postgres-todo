from src.utils.web import raise_404_if_none
from src.repository import make_sqlalchemy_repo
from src import database as db
from .schemas import User


repo = make_sqlalchemy_repo()


async def create_user(user_scheme: User) -> int:
    data = db.UserModel(**user_scheme.__dict__)
    return await repo.add(data)


async def get_user_by_id(user_id: int) -> User:
    user = await repo.get(db.UserModel, pk=user_id)
    await raise_404_if_none(
        user,
        message=f'User with id \'{user_id}\' does not exist'
    )
    user_scheme = User(**user.__dict__)
    return user_scheme


async def get_user_list(limit: int = None) -> list[User]:
    users = await repo.list(db.UserModel, limit=limit)
    return [User(**user.__dict__) for user in users]


async def update_user(user: User, user_id: int) -> None:
    updated_user = await repo.update(
        db.UserModel,
        pk=user_id,
        values=user.__dict__
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
