import asyncio

import pytest

from src.core.database import UserModel, NoteModel, init_models


asyncio.run(init_models())


@pytest.mark.asyncio
async def test_add_user(repo, get_db_user):
    get_db_user.email = 'another@example.com'
    user_id = await repo.add(get_db_user)
    assert isinstance(user_id, int)


@pytest.mark.asyncio
async def test_get_user(repo):
    user = await repo.get(UserModel, 1)
    assert isinstance(user.username, str)


@pytest.mark.asyncio
async def test_add_note(repo, get_db_note):
    note_id = await repo.add(get_db_note)
    assert isinstance(note_id, int)


@pytest.mark.asyncio
async def test_get_note(repo):
    note = await repo.get(NoteModel, 1)
    assert note is not None
