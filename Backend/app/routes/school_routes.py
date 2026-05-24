from fastapi import APIRouter, Depends, HTTPException
from ..deps import admin_required
from ..services.school_service import create_school, list_schools

router = APIRouter(prefix="/schools", tags=["schools"])


@router.post('/')
async def create_school_route(payload: dict, _=Depends(admin_required)):
    sid = await create_school(payload)
    return {'id': sid}


@router.get('/')
async def list_schools_route():
    return await list_schools()
