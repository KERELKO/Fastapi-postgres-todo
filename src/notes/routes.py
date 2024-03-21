from fastapi import APIRouter, Depends

from src.auth.backend import current_active_user, admin
from src.database import UserModel
from .schemas import NoteCreate, NoteOut, NoteUpdate
from . import service


router = APIRouter(tags=['notes'], prefix='/notes')


@router.get('/my', response_model=list[NoteOut])
async def my_notes(
    user: UserModel = Depends(current_active_user)
) -> list[NoteOut]:
    notes = await service.get_filtered_notes(filters={'author_id': user.id})
    return notes


@router.get('/list', response_model=list[NoteOut])
async def get_note_list(
    user: UserModel = Depends(admin), limit: int = None
) -> list[NoteOut]:
    notes = await service.get_note_list(limit)
    return notes


@router.get('/{note_id}', response_model=NoteOut)
async def get_note(note_id: int, user: UserModel = Depends(admin)) -> NoteOut:
    note = await service.get_note(note_id)
    return note


@router.post('/create', response_model=NoteOut)
async def create_note(
    note_data: NoteCreate, user: UserModel = Depends(current_active_user)
) -> NoteOut:
    data = note_data.__dict__
    data['author_id'] = user.id
    new_note = await service.create_note(data)
    return new_note


@router.patch('/update/{note_id}', response_model=dict)
async def update_note(data: NoteUpdate, note_id: int) -> dict:
    await service.update_note(data=data.__dict__, note_id=note_id)
    return {'status': 'OK', 'message': 'Note updated successfully'}


@router.delete('/delete/{note_id}', response_model=dict)
async def delete_note(note_id: int) -> dict:
    await service.delete_note(note_id)
    return {'status': 'OK', 'message': 'Note deleted successfully'}
