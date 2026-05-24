from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from ..deps import get_current_user
from ..services.homework_service import assign_homework, submit_homework, list_my_homework, list_batch_homework, evaluate_homework, delete_homework
from ..schemas.homework_schema import HomeworkAssignRequest, HomeworkEvaluateRequest
from typing import Optional

router = APIRouter(prefix="/homework", tags=["homework"])


def _role_allowed(user: dict):
    return user.get('role') in ('admin', 'school_admin', 'teacher')


@router.post('/assign')
async def assign(request: HomeworkAssignRequest, user=Depends(get_current_user)):
    if not _role_allowed(user):
        raise HTTPException(status_code=403, detail='Forbidden')
    hid = await assign_homework(request.batchId, request.title, request.description, request.subject, request.dueDate, request.sessionId)
    return {'id': hid}


@router.post('/upload')
async def upload(homeworkId: Optional[str] = Form(None), file: UploadFile = File(...), user=Depends(get_current_user)):
    # student uploads a submission; homeworkId can be the assignment id to link
    content = await file.read()
    if len(content) > 25 * 1024 * 1024:
        raise HTTPException(status_code=400, detail='File too large')
    extra = {'assignmentId': homeworkId}
    sid = await submit_homework(homeworkId, user.get('id'), file.filename, content, extra)
    return {'id': sid}


@router.get('/my')
async def my_homework(user=Depends(get_current_user)):
    items = await list_my_homework(user.get('id'))
    return items


@router.get('/batch/{batchId}')
async def batch_homework(batchId: str, user=Depends(get_current_user)):
    items = await list_batch_homework(batchId)
    return items


@router.put('/{homeworkId}/evaluate')
async def evaluate(homeworkId: str, request: HomeworkEvaluateRequest, user=Depends(get_current_user)):
    if not _role_allowed(user):
        raise HTTPException(status_code=403, detail='Forbidden')
    await evaluate_homework(homeworkId, request.marks, request.feedback, request.status)
    return {'ok': True}


@router.delete('/{homeworkId}')
async def delete(homeworkId: str, user=Depends(get_current_user)):
    if not _role_allowed(user):
        raise HTTPException(status_code=403, detail='Forbidden')
    ok = await delete_homework(homeworkId)
    if not ok:
        raise HTTPException(status_code=404, detail='Not found')
    return {'ok': True}
