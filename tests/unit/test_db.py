import asyncio

import pytest

from src.repository import SQLAlchemyRepository
from src.database import engine, UserModel, NoteModel, init_models


asyncio.run(init_models())


@pytest.mark.asyncio
async def test_add_user():
    repo = SQLAlchemyRepository(engine)
    user = UserModel(username='user1', email='user@example.com')
    await repo.add(user)


@pytest.mark.asyncio
async def test_get_user():
    repo = SQLAlchemyRepository(engine)
    user = await repo.get(UserModel, 1)
    assert user.username == 'user1'
