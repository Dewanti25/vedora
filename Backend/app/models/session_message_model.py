from datetime import datetime
from typing import Optional


def session_message_document(
    sessionId: str,
    message: str,
    senderType: str = 'STUDENT',
    studentId: Optional[str] = None,
    teacherId: Optional[str] = None,
    messageType: str = 'TEXT',
):
    return {
        'sessionId': sessionId,
        'studentId': studentId,
        'teacherId': teacherId,
        'senderType': senderType,
        'message': message,
        'messageType': messageType,
        'createdAt': datetime.utcnow(),
    }
