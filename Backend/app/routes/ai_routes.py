from fastapi import APIRouter, Depends, HTTPException
from ..deps import get_current_user
from ..services.ai_service import (
    answer_student_doubt,
    generate_syllabus_plan as svc_generate_syllabus,
    generate_homework as svc_generate_homework,
    evaluate_homework as svc_evaluate_homework,
    generate_quiz as svc_generate_quiz,
    detect_weak_topics as svc_detect_weak_topics,
    generate_session_summary as svc_generate_session_summary,
)
from typing import Dict, Any

router = APIRouter(prefix="/ai", tags=["ai"])


def _role_allowed(user: dict):
    return user.get('role') in ('admin', 'school_admin', 'teacher')


@router.post('/chat')
async def chat(payload: Dict[str, Any], user=Depends(get_current_user)):
    prompt = payload.get('prompt')
    if not prompt:
        raise HTTPException(status_code=400, detail='prompt required')
    return await answer_student_doubt(prompt, user=user, context=payload.get('context'))


@router.post('/generate-syllabus')
async def generate_syllabus(payload: Dict[str, Any], user=Depends(get_current_user)):
    if not _role_allowed(user):
        raise HTTPException(status_code=403, detail='Forbidden')
    chapters = payload.get('chapters', [])
    params = payload.get('params', {})
    return await svc_generate_syllabus(chapters, params)


@router.post('/generate-homework')
async def generate_homework(payload: Dict[str, Any], user=Depends(get_current_user)):
    if not _role_allowed(user):
        raise HTTPException(status_code=403, detail='Forbidden')
    chapters = payload.get('chapters', [])
    params = payload.get('params', {})
    return await svc_generate_homework(chapters, params)


@router.post('/evaluate-homework')
async def evaluate_homework(payload: Dict[str, Any], user=Depends(get_current_user)):
    if not _role_allowed(user):
        raise HTTPException(status_code=403, detail='Forbidden')
    submission = payload.get('submission', {})
    return await svc_evaluate_homework(submission)


@router.post('/generate-quiz')
async def generate_quiz(payload: Dict[str, Any], user=Depends(get_current_user)):
    if not _role_allowed(user):
        raise HTTPException(status_code=403, detail='Forbidden')
    chapters = payload.get('chapters', [])
    params = payload.get('params', {})
    return await svc_generate_quiz(chapters, params)


@router.post('/detect-weak-topics')
async def detect_weak_topics(payload: Dict[str, Any], user=Depends(get_current_user)):
    # teacher/admin or student can request
    history = payload.get('history', {})
    return await svc_detect_weak_topics(history)


@router.post('/session-summary')
async def session_summary(payload: Dict[str, Any], user=Depends(get_current_user)):
    messages = payload.get('messages', [])
    return await svc_generate_session_summary(messages)
from fastapi import APIRouter

router = APIRouter(prefix="/ai", tags=["ai"])


@router.post('/generate-syllabus')
async def generate_syllabus():
    return {'ok': True, 'plan_id': 'demo'}


@router.post('/teach-session')
async def teach_session():
    return {'ok': True}
