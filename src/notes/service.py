from pydantic import ValidationError

from src.utils.web import raise_404_if_none
from src import database as db
from src.auth.service import get_user_by_id
from src.repository import make_sqlalchemy_repo
from src.notes.schemas import Note


repo = make_sqlalchemy_repo()


async def get_note_list(limit: int = None) -> list[Note]:
    notes = await repo.list(db.NoteModel, limit=limit)
    return [Note(**note.__dict__) for note in notes]


async def create_note(note: Note) -> Note:
    author = await get_user_by_id(note.author_id)
    await raise_404_if_none(
        author,
        message=f'Author with id \'{note.author_id}\' does not exist'
    )
    note_id = await repo.add(db.NoteModel(**note.__dict__))
    if note_id:
        return note
    else:
        raise ValidationError


async def get_note(note_id: int) -> Note:
    note = await repo.get(db.NoteModel, note_id)
    await raise_404_if_none(
        note,
        message=f'Note with id \'{note_id}\' not found'
    )
    return Note(**note.__dict__)


async def update_note(note: Note, note_id: int) -> None:
    await repo.update(db.NoteModel, pk=note_id, values=note.__dict__)


async def delete_note(note_id: int) -> int:
    deleted_note_id = await repo.delete(db.NoteModel, pk=note_id)
    await raise_404_if_none(
        deleted_note_id,
        message=f'Note with id \'{note_id}\' not found'
    )
    return deleted_note_id
