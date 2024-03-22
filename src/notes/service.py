from src.core import database as db
from src.utils.web import raise_404_if_none
from src.core.repository import make_sqlalchemy_repo
from src.notes.schemas import (
    BaseNoteModel,
    NoteOut,
    BaseNoteOutModel,
)


repo = make_sqlalchemy_repo()


async def get_filtered_notes(
    filters: dict, limit: int = None, scheme: BaseNoteModel = NoteOut,
) -> list[BaseNoteModel]:
    notes = await repo.filter_by(db.NoteModel, filters, limit)
    return [scheme(**note.__dict__) for note in notes]


async def get_note_list(
    limit: int = None, scheme: BaseNoteModel = NoteOut
) -> list[BaseNoteModel]:
    notes = await repo.get_all(db.NoteModel, limit=limit)
    return [scheme(**note.__dict__) for note in notes]


async def create_note(
    data: dict, scheme: BaseNoteOutModel = NoteOut
) -> BaseNoteOutModel:
    data_id = await repo.add(db.NoteModel(**data))
    return scheme(**data, id=data_id)


async def get_note(
    note_id: int, scheme: BaseNoteModel = NoteOut
) -> BaseNoteOutModel:
    note = await repo.get(db.NoteModel, note_id)
    raise_404_if_none(
        note,
        message=f'Note with id \'{note_id}\' not found'
    )
    return scheme(**note.__dict__)


async def update_note(
    data: dict, note_id: int, scheme: NoteOut = NoteOut
) -> NoteOut:
    updated_note = await repo.update(db.NoteModel, pk=note_id, values=data)
    return scheme(**updated_note.__dict__)


async def delete_note(note_id: int) -> int:
    deleted_note_id = await repo.delete(db.NoteModel, pk=note_id)
    await raise_404_if_none(
        deleted_note_id,
        message=f'Note with id \'{note_id}\' not found'
    )
    return deleted_note_id
