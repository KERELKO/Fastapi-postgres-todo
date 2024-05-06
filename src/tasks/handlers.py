from fastapi import APIRouter, Depends, HTTPException

from src.auth.config import current_active_user, is_admin
from src.auth.schemas import UserRead
from src.core.exceptions import ApplicationException
from src.tasks.exceptions import AuthorDoesNotExist, TaskDoesNotExist
from src.tasks.services import TaskService

from .schemas import TaskCreate, TaskRead, TaskUpdate


router = APIRouter(tags=['tasks'], prefix='/tasks')


@router.get('/my', response_model=list[TaskRead])
async def my_tasks(
    completed: bool = False,
    limit: int = 0,
    user: UserRead = Depends(current_active_user),
) -> list[TaskRead]:
    service = TaskService()
    filters = {'author_id': user.id}
    if type(completed) == bool:
        filters['completed'] = completed
    try:
        tasks = await service.filter_tasks(filters=filters, limit=limit)
    except ApplicationException as e:
        raise HTTPException(status_code=400, detail=e)
    return tasks


@router.get('', response_model=list[TaskRead])
async def get_task_list(
    limit: int = None,
    user: UserRead = Depends(is_admin),
) -> list[TaskRead]:
    service = TaskService()
    tasks = await service.get_all_tasks(limit)
    return tasks


@router.get('/{task_id}', response_model=TaskRead)
async def get_task(
    task_id: int,
    user: UserRead = Depends(current_active_user),
) -> TaskRead:
    service = TaskService()
    try:
        task = await service.get_task_by_id(task_id, user)
    except TaskDoesNotExist as e:
        raise HTTPException(status_code=404, detail=e.message)
    return task


@router.post('', response_model=TaskRead)
async def create_task(
    task_data: TaskCreate,
    user: UserRead = Depends(current_active_user),
) -> TaskRead:
    service = TaskService()
    task_data.author_id = user.id
    try:
        new_task = await service.create_task(task_data)
    except AuthorDoesNotExist as e:
        raise HTTPException(status_code=404, detail=e.message)
    return new_task


@router.patch('/{task_id}', response_model=TaskRead)
async def update_task(
    values: TaskUpdate,
    task_id: int,
    user: UserRead = Depends(current_active_user)
) -> TaskRead:
    service = TaskService()
    try:
        updated_task = await service.update_task(
            values=values.model_dump(), task_id=task_id, user=user
        )
    except TaskDoesNotExist as e:
        raise HTTPException(status_code=404, detail=e.message)
    except ApplicationException as e:
        raise HTTPException(status_code=404, detail=e)
    return updated_task


@router.delete('/{task_id}', response_model=dict[str, str])
async def delete_task(
    task_id: int,
    user: UserRead = Depends(current_active_user),
) -> dict[str, str]:
    service = TaskService()
    try:
        await service.delete_task(task_id, user)
    except TaskDoesNotExist as e:
        raise HTTPException(status_code=404, detail=e.message)
    except ApplicationException as e:
        raise HTTPException(status_code=400, detail=e)
    return {
        'completed': 'OK',
        'message': f'task with id \'{task_id}\' was deleted successfully'
    }
