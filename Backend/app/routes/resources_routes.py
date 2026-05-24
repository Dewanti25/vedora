from fastapi import APIRouter

router = APIRouter(prefix="/resources", tags=["resources"])


@router.get('/')
async def list_resources():
    return {
        'resources': [
            'users','schools','boards','grades','subjects','courses','chapters','batches','enrollments',
            'class_schedules','live_sessions','session_messages','homework','notes','quizzes','quiz_attempts',
            'student_progress','textbooks','ai_memories','subscriptions','payments','notifications'
        ]
    }
