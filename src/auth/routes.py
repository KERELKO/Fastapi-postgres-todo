from fastapi import APIRouter, status, HTTPException

from .schemas import User
from . import service

router = APIRouter(tags=['auth'], prefix='/users')


@router.post(
    '/create',
    response_model=int,
    responses={
        status.HTTP_200_OK: {
            'description': 'Returns the "id" of the created user in the database',
        },
    }
)
async def register_user(user: User) -> int:
    user_id = await service.create_user(user)
    return user_id


@router.get('/list', response_model=list[User])
async def get_user_list(limit: int = None) -> list[User]:
    users = await service.get_user_list(limit)
    return users


@router.get('/{user_id}', response_model=User)
async def get_user(user_id: int) -> User:
    user = await service.get_user_by_id(user_id)
    if not user:
        HTTPException(status_code=404, detail=f'User not with id \'{user_id}\' found')
    return user
