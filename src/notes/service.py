from fastapi import HTTPException

from pydantic import ValidationError

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
    if not author:
        raise HTTPException(
            status_code=404,
            detail=f'Author with id \'{note.author_id}\' does not exist'
        )
    note_id = await repo.add(db.NoteModel(**note.__dict__))
    if note_id:
        return note
    else:
        raise ValidationError


async def get_note(note_id: int) -> Note:
    note = await repo.get(db.NoteModel, note_id)
    if not note:
        raise HTTPException(status_code=404, detail='Note not found')
    return Note(**note.__dict__)
