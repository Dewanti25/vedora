from datetime import datetime
from typing import Optional


def textbook_document(
    bookTitle: str,
    uploadedBy: str,
    board: str,
    grade: str,
    subject: str,
    fileName: str,
    fileUrl: Optional[str] = None,
    fileType: Optional[str] = 'application/pdf',
    fileSize: Optional[int] = 0,
    processingStatus: str = 'UPLOADED',
    extractedText: Optional[str] = None,
    chaptersExtracted: bool = False,
    schoolId: Optional[str] = None,
):
    now = datetime.utcnow()
    return {
        'schoolId': schoolId,
        'uploadedBy': uploadedBy,
        'board': board,
        'grade': grade,
        'subject': subject,
        'bookTitle': bookTitle,
        'fileUrl': fileUrl,
        'fileName': fileName,
        'fileType': fileType,
        'fileSize': fileSize,
        'processingStatus': processingStatus,
        'extractedText': extractedText,
        'chaptersExtracted': chaptersExtracted,
        'createdAt': now,
    }
