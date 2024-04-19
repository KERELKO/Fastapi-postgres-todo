from fastapi import APIRouter, Depends

from src.auth.config import current_active_user, is_admin
from src.auth.schemas import UserRead
from src.services.tasks import TasksService

from .schemas import TaskCreate, TaskRead, TaskUpdate


router = APIRouter(tags=['tasks'], prefix='/tasks')
service = TasksService()


@router.get('/my', response_model=list[TaskRead])
async def my_tasks(
    completed: bool = False,
    limit: int | None = None,
    user: UserRead = Depends(current_active_user)
) -> list[TaskRead]:
    filters = {'author_id': user.id}
    if completed is not None:
        filters['completed'] = completed
    tasks = await service.filter_tasks(filters=filters, limit=limit)
    return tasks


@router.get('', response_model=list[TaskRead])
async def get_task_list(
    user: UserRead = Depends(is_admin), limit: int = None
) -> list[TaskRead]:
    tasks = await service.get_all_tasks(limit)
    return tasks


@router.get('/{task_id}', response_model=TaskRead)
async def get_task(
    task_id: int, user: UserRead = Depends(current_active_user),
) -> TaskRead:
    task = await service.get_task_by_id(task_id, user)
    return task


@router.post('', response_model=TaskRead)
async def create_task(
    task_data: TaskCreate, user: UserRead = Depends(current_active_user)
) -> TaskRead:
    task_data.author_id = user.id
    new_task = await service.create_task(task_data)
    return new_task


@router.patch('{task_id}', response_model=TaskRead)
async def update_task(
    values: TaskUpdate,
    task_id: int,
    user: UserRead = Depends(current_active_user)
) -> TaskRead:
    updated_task = await service.update_task(
        values=values.model_dump(), task_id=task_id, user=user
    )
    return updated_task


@router.delete('{task_id}', response_model=dict)
async def delete_task(
    task_id: int, user: UserRead = Depends(current_active_user)
) -> dict:
    await service.delete_task(task_id, user)
    return {
        'completed': 'OK',
        'message': f'task with id \'{task_id}\' was deleted successfully'
    }
