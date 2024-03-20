from fastapi import APIRouter

from .schemas import User
from . import service

router = APIRouter(tags=['auth'], prefix='/users')


@router.get('/list', response_model=list[User])
async def get_list_of_all_users(limit: int = None) -> list[User]:
    users = await service.get_user_list(limit)
    return users


@router.get('/{user_id}', response_model=User)
async def get_particular_user(user_id: int) -> User:
    user = await service.get_user_by_id(user_id)
    return user


@router.post('/create', response_model=dict)
async def register_new_user(user: User) -> dict:
    await service.create_user(user)
    return {'status': 'OK', 'message': 'User created successfully'}


@router.patch('/update/{user_id}', response_model=dict)
async def update_user_info(user: User, user_id: int):
    await service.update_user(user=user, user_id=user_id)
    return {'status': 'OK', 'message': 'User updated successfully'}


@router.delete('/delete/{user_id}', response_model=dict)
async def delete_user(user_id: int) -> dict:
    await service.delete_user(user_id)
    return {'status': 'OK', 'message': 'User deleted successfully'}
