from datetime import datetime
from typing import Optional


def live_session_document(
    batchId: str,
    courseId: str,
    topic: str,
    sessionDate: str,
    startTime: str,
    endTime: str,
    chapterId: Optional[str] = None,
    status: str = 'UPCOMING',
    aiTeacherId: Optional[str] = None,
    summary: Optional[str] = None,
    homeworkGenerated: bool = False,
    createdBy: Optional[str] = None,
):
    return {
        'batchId': batchId,
        'courseId': courseId,
        'chapterId': chapterId,
        'topic': topic,
        'sessionDate': sessionDate,
        'startTime': startTime,
        'endTime': endTime,
        'status': status,
        'aiTeacherId': aiTeacherId,
        'summary': summary,
        'homeworkGenerated': homeworkGenerated,
        'participants': [],
        'createdBy': createdBy,
        'createdAt': datetime.utcnow(),
    }
