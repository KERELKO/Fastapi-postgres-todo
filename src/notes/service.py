from pydantic import ValidationError

from src.utils.web import raise_404_if_none
from src import database as db
from src.auth.service import get_user_by_id
from src.repository import make_sqlalchemy_repo
from src.notes.schemas import (
    BaseNoteModel,
    NoteCreate,
    NoteUpdate,
    NoteOut,
    BaseNoteOutModel,
)


repo = make_sqlalchemy_repo()


async def get_note_list(
    limit: int = None, scheme: BaseNoteModel = NoteOut
) -> list[BaseNoteModel]:
    notes = await repo.list(db.NoteModel, limit=limit)
    return [scheme(**note.__dict__) for note in notes]


async def create_note(
    data: NoteCreate, scheme: BaseNoteOutModel = NoteOut
) -> BaseNoteOutModel:
    author = await get_user_by_id(data.author_id)
    await raise_404_if_none(
        author,
        message=f'Author with id \'{data.author_id}\' does not exist'
    )
    data_id = await repo.add(db.NoteModel(**data.__dict__))
    if data_id:
        return scheme(**data.__dict__, id=data_id)
    else:
        raise ValidationError


async def get_note(
    note_id: int, scheme: BaseNoteModel = NoteOut
) -> BaseNoteOutModel:
    note = await repo.get(db.NoteModel, note_id)
    await raise_404_if_none(
        note,
        message=f'Note with id \'{note_id}\' not found'
    )
    return scheme(**note.__dict__)


async def update_note(data: NoteUpdate, note_id: int) -> None:
    await repo.update(db.NoteModel, pk=note_id, values=data.__dict__)


async def delete_note(note_id: int) -> int:
    deleted_note_id = await repo.delete(db.NoteModel, pk=note_id)
    await raise_404_if_none(
        deleted_note_id,
        message=f'Note with id \'{note_id}\' not found'
    )
    return deleted_note_id
