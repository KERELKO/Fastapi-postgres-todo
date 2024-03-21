from fastapi import APIRouter

from .backend import fastapi_users, auth_backend
from .schemas import UserCreate, UserRead, UserUpdate
from . import service


router = APIRouter(tags=['auth'])

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix='/auth',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix='/auth',
    tags=['auth'],
)

user_router = APIRouter(tags=['users'])

user_router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix='/users',
    tags=['users'],
)
# @router.get('/list', response_model=list[UserOut])
# async def get_list_of_all_users(
#     limit: int = None
# ) -> list[UserOut]:
#     users = await service.get_user_list(limit=limit)
#     return users


@router.get('/{user_id}', response_model=UserRead)
async def get_particular_user(user_id: int) -> UserRead:
    user = await service.get_user_by_id(user_id)
    return user


# @router.post('/create', response_model=UserOut)
# async def register_new_user(user_data: UserCreate) -> UserOut:
#     new_user = await service.create_user(user_data)
#     return new_user


# @router.patch('/update/{user_id}', response_model=dict)
# async def update_user_info(user_data: UserCreate, user_id: int):
#     await service.update_user(user_id, user_data)
#     return {'status': 'OK', 'message': 'User updated successfully'}


# @router.delete('/delete/{user_id}', response_model=dict)
# async def delete_user(user_id: int) -> dict:
#     await service.delete_user(user_id)
#     return {'status': 'OK', 'message': 'User deleted successfully'}
