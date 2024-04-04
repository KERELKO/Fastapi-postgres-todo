from fastapi import APIRouter

from .config import fastapi_users, auth_backend
from .schemas import UserCreate, UserRead, UserUpdate


router = APIRouter(prefix='/auth', tags=['auth'])

router.include_router(fastapi_users.get_auth_router(auth_backend))
router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))

user_router = APIRouter(tags=['users'])

user_router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix='/users',
    tags=['users'],
)
