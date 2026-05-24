from fastapi import APIRouter, Depends, HTTPException
from ..deps import get_current_user
from ..services import schedule_service
from typing import List
from ..services.schedule_service import create_schedule, get_schedules_for_batch, get_schedule, update_schedule, delete_schedule, get_schedules_for_student

from ..services.user_service import get_user_by_id

router = APIRouter()


def _has_permission(user: dict):
    role = user.get('role')
    return role in ('ADMIN', 'SCHOOL_ADMIN', 'TEACHER')


@router.post('/batches/{batchId}/schedule')
async def create_batch_schedule(batchId: str, payload: dict, user=Depends(get_current_user)):
    if not _has_permission(user):
        raise HTTPException(status_code=403, detail='Not allowed')
    sid = await create_schedule(batchId, payload)
    return {'id': sid}


@router.get('/batches/{batchId}/schedule')
async def list_batch_schedule(batchId: str, user=Depends(get_current_user)):
    # students and others can view
    items = await get_schedules_for_batch(batchId)
    return items


@router.put('/schedules/{scheduleId}')
async def put_schedule(scheduleId: str, payload: dict, user=Depends(get_current_user)):
    if not _has_permission(user):
        raise HTTPException(status_code=403, detail='Not allowed')
    await update_schedule(scheduleId, payload)
    return {'ok': True}


@router.delete('/schedules/{scheduleId}')
async def del_schedule(scheduleId: str, user=Depends(get_current_user)):
    if not _has_permission(user):
        raise HTTPException(status_code=403, detail='Not allowed')
    await delete_schedule(scheduleId)
    return {'ok': True}


@router.get('/students/me/schedule')
async def student_schedule(user=Depends(get_current_user)):
    # only students need this endpoint but others can call too
    schedules = await get_schedules_for_student(user)
    return schedules
