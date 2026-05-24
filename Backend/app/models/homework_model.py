from datetime import datetime
from typing import Optional


def homework_document(
    batchId: str,
    title: str,
    description: str,
    subject: str,
    dueDate: str,
    sessionId: Optional[str] = None,
    studentId: Optional[str] = None,
    fileUrl: Optional[str] = None,
    status: str = 'ASSIGNED',
    submittedAt: Optional[str] = None,
    marks: Optional[float] = None,
    feedback: Optional[str] = None,
    createdAt: Optional[datetime] = None,
):
    return {
        'batchId': batchId,
        'sessionId': sessionId,
        'studentId': studentId,
        'title': title,
        'description': description,
        'subject': subject,
        'fileUrl': fileUrl,
        'status': status,
        'dueDate': dueDate,
        'submittedAt': submittedAt,
        'marks': marks,
        'feedback': feedback,
        'createdAt': createdAt or datetime.utcnow(),
    }
def homework_document(session_id: str, title: str, description: str) -> dict:
    return {
        'session_id': session_id,
        'title': title,
        'description': description,
        'createdAt': None,
    }
