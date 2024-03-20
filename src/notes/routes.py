from fastapi import APIRouter

from .schemas import Note
from . import service


router = APIRouter(tags=['notes'], prefix='/notes')


@router.get('/list', response_model=list[Note])
async def get_note_list(limit: int = None) -> list[Note]:
    notes = await service.get_note_list(limit)
    return notes


@router.get('/{note_id}', response_model=Note)
async def get_note(note_id: int) -> Note:
    note = await service.get_note(note_id)
    return note


@router.post('/create', response_model=Note)
async def create_note(note: Note) -> Note:
    new_note = await service.create_note(note)
    return new_note


@router.patch('/update/{note_id}', response_model=dict)
async def update_note(note: Note, note_id: int) -> dict:
    await service.update_note(note=note, note_id=note_id)
    return {'status': 'OK', 'message': 'Note updated successfully'}


@router.delete('/delete/{note_id}', response_model=dict)
async def delete_note(note_id: int) -> dict:
    await service.delete_note(note_id)
    return {'status': 'OK', 'message': 'Note deleted successfully'}
