from fastapi import APIRouter, Depends

from src.auth.config import current_active_user, is_admin
from src.core.database import UserModel
from .schemas import TaskCreate, TaskRead, TaskUpdate
from . import service


router = APIRouter(tags=['tasks'], prefix='/tasks')


@router.get('/my', response_model=list[TaskRead])
async def my_tasks(
    user: UserModel = Depends(current_active_user)
) -> list[TaskRead]:
    tasks = await service.get_filtered_tasks(filters={'author_id': user.id})
    return tasks


@router.get('/list', response_model=list[TaskRead])
async def get_task_list(
    user: UserModel = Depends(is_admin), limit: int = None
) -> list[TaskRead]:
    tasks = await service.get_task_list(limit)
    return tasks


@router.get('/{task_id}', response_model=TaskRead)
async def get_task(
    task_id: int, user: UserModel = Depends(current_active_user),
) -> TaskRead:
    task = await service.get_task(task_id, user)
    return task


@router.post('/create', response_model=TaskRead)
async def create_task(
    task_data: TaskCreate, user: UserModel = Depends(current_active_user)
) -> TaskRead:
    data = task_data.__dict__
    data['author_id'] = user.id
    new_task = await service.create_task(data)
    return new_task


@router.patch('/update/{task_id}', response_model=TaskRead)
async def update_task(
    data: TaskUpdate,
    task_id: int,
    user: UserModel = Depends(current_active_user)
) -> TaskRead:
    updated_task = await service.update_task(
        data=data.__dict__, task_id=task_id, user=user
    )
    return updated_task


@router.delete('/delete/{task_id}', response_model=dict)
async def delete_task(
    task_id: int, user: UserModel = Depends(current_active_user)
) -> dict:
    await service.delete_task(task_id, user)
    return {
        'status': 'OK',
        'message': f'task with id \'{task_id}\' was deleted successfully'
    }
