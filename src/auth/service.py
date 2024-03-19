from src.repository import make_sqlalchemy_repo
from src import database as db
from .schemas import User


repo = make_sqlalchemy_repo()


async def create_user(user_scheme: User) -> int:
    data = db.UserModel(username=user_scheme.username, email=user_scheme.email)
    return await repo.add(data)


async def get_user_by_id(user_id: int) -> User | None:
    user = await repo.get(db.UserModel, pk=user_id)
    if not user:
        return None
    user_scheme = User(username=user.username, email=user.email)
    return user_scheme


async def get_user_list(limit: int = None) -> list[User]:
    users = await repo.list(db.UserModel, limit=limit)
    return [User(**user.__dict__) for user in users]
