from fastapi import APIRouter, Depends, HTTPException
from ..deps import get_current_user
from ..services.syllabus_service import generate_syllabus_plan, get_plan, approve_plan, list_plans_for_batch
from ..schemas.syllabus_schema import SyllabusGenerateRequest
from bson import ObjectId

router = APIRouter(prefix="/syllabus", tags=["syllabus"])


def _check_role_allowed(user: dict):
    return user.get('role') in ('admin', 'school_admin', 'teacher')


@router.post('/generate')
async def generate(request: SyllabusGenerateRequest, user=Depends(get_current_user)):
    if not _check_role_allowed(user):
        raise HTTPException(status_code=403, detail='Forbidden')
    planId = await generate_syllabus_plan(request.batchId, request.courseId, request.startDate, request.endDate, request.examDate, request.classesPerWeek, request.generatedBy)
    return {'id': planId}


@router.get('/{planId}')
async def get_plan_route(planId: str, user=Depends(get_current_user)):
    p = await get_plan(planId)
    if not p:
        raise HTTPException(status_code=404, detail='Not found')
    p['id'] = str(p['_id'])
    return p


@router.put('/{planId}/approve')
async def approve(planId: str, user=Depends(get_current_user)):
    if not _check_role_allowed(user):
        raise HTTPException(status_code=403, detail='Forbidden')
    await approve_plan(planId, user.get('id'))
    return {'ok': True}


@router.get('/batches/{batchId}/syllabus')
async def list_for_batch(batchId: str, user=Depends(get_current_user)):
    # allow teachers/students to view; enforce auth
    plans = await list_plans_for_batch(batchId)
    return plans


# expose the path requested: /batches/{batchId}/syllabus
router_alt = APIRouter()


@router_alt.get('/batches/{batchId}/syllabus')
async def list_for_batch_alt(batchId: str, user=Depends(get_current_user)):
    plans = await list_plans_for_batch(batchId)
    return plans
