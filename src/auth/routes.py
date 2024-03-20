from fastapi import APIRouter

from .schemas import UserCreate, UserOut
from . import service


router = APIRouter(tags=['auth'], prefix='/users')


@router.get('/list', response_model=list[UserOut])
async def get_list_of_all_users(
    limit: int = None
) -> list[UserOut]:
    users = await service.get_user_list(limit=limit)
    return users


@router.get('/{user_id}', response_model=UserOut)
async def get_particular_user(user_id: int) -> UserOut:
    user = await service.get_user_by_id(user_id)
    return user


@router.post('/create', response_model=UserOut)
async def register_new_user(user_data: UserCreate) -> UserOut:
    new_user = await service.create_user(user_data)
    return new_user


@router.patch('/update/{user_id}', response_model=dict)
async def update_user_info(user_data: UserCreate, user_id: int):
    await service.update_user(user_id, user_data)
    return {'status': 'OK', 'message': 'User updated successfully'}


@router.delete('/delete/{user_id}', response_model=dict)
async def delete_user(user_id: int) -> dict:
    await service.delete_user(user_id)
    return {'status': 'OK', 'message': 'User deleted successfully'}
