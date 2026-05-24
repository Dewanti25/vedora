from fastapi import APIRouter, Depends, HTTPException
from ..deps import get_current_user
from ..schemas.quiz_schema import QuizCreateRequest, AttemptRequest
from ..services.quiz_service import create_quiz, list_quizzes, get_quiz, submit_attempt, list_student_attempts

router = APIRouter(prefix="/quizzes", tags=["quizzes"])


def _role_allowed(user: dict):
    return user.get('role') in ('admin', 'school_admin', 'teacher')


@router.post('')
async def create(request: QuizCreateRequest, user=Depends(get_current_user)):
    if not _role_allowed(user):
        raise HTTPException(status_code=403, detail='Forbidden')
    qid = await create_quiz(request.batchId, request.courseId, request.title, [q.dict() for q in request.questions], request.durationMinutes, user.get('id'), request.chapterId)
    return {'id': qid}


@router.get('')
async def list_route(user=Depends(get_current_user)):
    items = await list_quizzes()
    return items


@router.get('/{quizId}')
async def get_route(quizId: str, user=Depends(get_current_user)):
    q = await get_quiz(quizId)
    if not q:
        raise HTTPException(status_code=404, detail='Not found')
    q['id'] = str(q['_id'])
    return q


@router.post('/{quizId}/attempt')
async def attempt_route(quizId: str, request: AttemptRequest, user=Depends(get_current_user)):
    # student submits
    student = user
    res = await submit_attempt(quizId, student.get('id'), [a.dict() for a in request.answers])
    if not res:
        raise HTTPException(status_code=404, detail='Quiz not found')
    return res


@router.get('/students/me/quiz-results')
async def results_route(user=Depends(get_current_user)):
    items = await list_student_attempts(user.get('id'))
    return items
