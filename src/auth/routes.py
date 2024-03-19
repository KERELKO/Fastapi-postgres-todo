from fastapi import APIRouter, status

from .schemas import User
from . import service

router = APIRouter(tags=['auth'], prefix='/auth')


@router.post(
    '/user/create',
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


@router.get('/user/list', response_model=list[User])
async def get_user_list(limit: int = None) -> list[User]:
    users = await service.get_user_list(limit)
    return users


@router.get('/user/{user_id}', response_model=User)
async def get_user(user_id: int) -> User:
    user = await service.get_user_by_id(user_id)
    return user
