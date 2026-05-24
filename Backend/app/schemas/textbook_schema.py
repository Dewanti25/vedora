from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class TextbookOut(BaseModel):
    id: str
    schoolId: Optional[str]
    uploadedBy: str
    board: Optional[str]
    grade: Optional[str]
    subject: Optional[str]
    bookTitle: str
    fileUrl: Optional[str]
    fileName: str
    fileType: Optional[str]
    fileSize: Optional[int]
    processingStatus: str
    extractedText: Optional[str]
    chaptersExtracted: bool
    chapters: Optional[List[dict]]
    createdAt: Optional[datetime]
