from fastapi import APIRouter, Depends, HTTPException
from ..deps import admin_required, get_current_user, student_required
from ..database import db
from bson import ObjectId
from ..services.batch_service import create_batch, list_batches, join_batch_atomic

router = APIRouter(prefix="/batches", tags=["batches"])


@router.post('/')
async def create_batch_route(payload: dict, _=Depends(admin_required)):
    batch_id = await create_batch(payload)
    return {'id': batch_id}


@router.get('/')
async def list_batches_route():
    items = await list_batches()
    return items


@router.post('/{batch_id}/join')
async def join_batch_route(batch_id: str, user=Depends(student_required)):
    result = await join_batch_atomic(batch_id, user)
    status = result.get('status')
    if status == 'already_enrolled':
        return {'ok': True, 'message': 'Already enrolled'}
    if status == 'not_found':
        raise HTTPException(status_code=404, detail='Batch not found')
    if status == 'full':
        raise HTTPException(status_code=400, detail='Batch full')
    if status == 'enrolled':
        return {'ok': True}
    raise HTTPException(status_code=500, detail='Unable to join')
