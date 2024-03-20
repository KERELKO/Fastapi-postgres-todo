from fastapi import APIRouter

from .schemas import NoteCreate, NoteOut, NoteUpdate
from . import service


router = APIRouter(tags=['notes'], prefix='/notes')


@router.get('/list', response_model=list[NoteOut])
async def get_note_list(limit: int = None) -> list[NoteOut]:
    notes = await service.get_note_list(limit)
    return notes


@router.get('/{note_id}', response_model=NoteOut)
async def get_note(note_id: int) -> NoteOut:
    note = await service.get_note(note_id)
    return note


@router.post('/create', response_model=NoteOut)
async def create_note(data: NoteCreate) -> NoteOut:
    new_note = await service.create_note(data)
    return new_note


@router.patch('/update/{note_id}', response_model=dict)
async def update_note(data: NoteUpdate, note_id: int) -> dict:
    await service.update_note(data=data, note_id=note_id)
    return {'status': 'OK', 'message': 'Note updated successfully'}


@router.delete('/delete/{note_id}', response_model=dict)
async def delete_note(note_id: int) -> dict:
    await service.delete_note(note_id)
    return {'status': 'OK', 'message': 'Note deleted successfully'}
