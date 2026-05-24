from fastapi import APIRouter, Depends, HTTPException
from ..deps import get_current_user
from ..services.live_session_service import create_session, get_session, add_participant, remove_participant, complete_session
from ..services.session_message_service import save_message, list_messages, generate_ai_response
from bson import ObjectId

router = APIRouter(prefix="/sessions", tags=["sessions"])


def _has_permission(user: dict):
    return user.get('role') in ('ADMIN', 'SCHOOL_ADMIN', 'TEACHER')


@router.post('')
async def post_session(payload: dict, user=Depends(get_current_user)):
    if not _has_permission(user):
        raise HTTPException(status_code=403, detail='Not allowed')
    payload['createdAt'] = __import__('datetime').datetime.utcnow()
    sid = await create_session(payload, created_by=user.get('id'))
    return {'id': sid}


@router.get('/{sessionId}')
async def get_session_route(sessionId: str, user=Depends(get_current_user)):
    s = await get_session(sessionId)
    if not s:
        raise HTTPException(status_code=404, detail='Session not found')
    s['id'] = str(s.get('_id'))
    return s


@router.post('/{sessionId}/join')
async def join_session(sessionId: str, user=Depends(get_current_user)):
    await add_participant(sessionId, user.get('id') or str(user.get('_id')))
    return {'ok': True}


@router.post('/{sessionId}/leave')
async def leave_session(sessionId: str, user=Depends(get_current_user)):
    await remove_participant(sessionId, user.get('id') or str(user.get('_id')))
    return {'ok': True}


@router.post('/{sessionId}/message')
async def post_message(sessionId: str, payload: dict, user=Depends(get_current_user)):
    # payload: { message: str, messageType?: 'TEXT' }
    message = payload.get('message')
    if not message:
        raise HTTPException(status_code=400, detail='No message')
    student_id = user.get('id') or str(user.get('_id'))
    # save student message
    mid = await save_message(sessionId, message, senderType='STUDENT', studentId=student_id, messageType=payload.get('messageType', 'TEXT'))
    # generate AI response (dummy)
    ai = await generate_ai_response(sessionId, message)
    return {'messageId': mid, 'ai': ai}


@router.get('/{sessionId}/messages')
async def get_messages(sessionId: str, user=Depends(get_current_user)):
    msgs = await list_messages(sessionId)
    return msgs


@router.post('/{sessionId}/complete')
async def complete_session_route(sessionId: str, payload: dict = None, user=Depends(get_current_user)):
    if not _has_permission(user):
        raise HTTPException(status_code=403, detail='Not allowed')
    summary = None
    if payload:
        summary = payload.get('summary')
    await complete_session(sessionId, summary=summary)
    return {'ok': True}
