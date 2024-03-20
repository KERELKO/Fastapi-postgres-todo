import asyncio

import pytest

from src.database import UserModel, NoteModel, init_models


asyncio.run(init_models())


@pytest.mark.asyncio
async def test_add_user(repo):
    user = UserModel(username='user1', email='user@example.com')
    user_id = await repo.add(user)
    assert isinstance(user_id, int)


@pytest.mark.asyncio
async def test_get_user(repo):
    user = await repo.get(UserModel, 1)
    assert user.username == 'user1'


@pytest.mark.asyncio
async def test_add_note(repo, note_data):
    note = NoteModel(**note_data)
    note_id = await repo.add(note)
    assert note_id is not None


@pytest.mark.asyncio
async def test_get_note(repo):
    note = await repo.get(NoteModel, 1)
    assert note is not None
