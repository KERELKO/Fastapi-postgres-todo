from fastapi import APIRouter

from .schemas import Note
from . import service


router = APIRouter(tags=['notes'], prefix='/notes')


@router.post('/create', response_model=Note)
async def create_note(note: Note) -> Note:
    new_note = await service.create_note(note)
    return new_note


@router.get('/list', response_model=list[Note])
async def get_note_list(limit: int = None) -> list[Note]:
    notes = await service.get_note_list(limit)
    return notes


@router.get('/{note_id}', response_model=Note)
async def get_note(note_id: int) -> Note:
    note = await service.get_note(note_id)
    return note
