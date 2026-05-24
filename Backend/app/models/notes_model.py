from datetime import datetime
from typing import Optional


def notes_document(
    title: str,
    board: str,
    grade: str,
    subject: str,
    fileUrl: str,
    fileType: str,
    fileSize: int,
    uploadedBy: str,
    createdAt: Optional[datetime] = None,
):
    return {
        'title': title,
        'board': board,
        'grade': grade,
        'subject': subject,
        'fileUrl': fileUrl,
        'fileType': fileType,
        'fileSize': fileSize,
        'uploadedBy': uploadedBy,
        'createdAt': createdAt or datetime.utcnow(),
    }
