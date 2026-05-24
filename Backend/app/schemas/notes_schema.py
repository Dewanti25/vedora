from pydantic import BaseModel
from typing import Optional


class NoteUploadRequest(BaseModel):
    title: str
    board: Optional[str] = ''
    grade: Optional[str] = ''
    subject: Optional[str] = ''


class NoteOut(BaseModel):
    id: str
    title: str
    board: Optional[str]
    grade: Optional[str]
    subject: Optional[str]
    fileUrl: Optional[str]
    fileType: Optional[str]
    fileSize: Optional[int]
    uploadedBy: Optional[str]
    createdAt: Optional[str]
