from pydantic import BaseModel
from typing import Optional


class HomeworkAssignRequest(BaseModel):
    batchId: str
    sessionId: Optional[str] = None
    title: str
    description: Optional[str] = ''
    subject: Optional[str] = ''
    dueDate: str


class HomeworkEvaluateRequest(BaseModel):
    marks: Optional[float] = None
    feedback: Optional[str] = None
    status: Optional[str] = 'EVALUATED'
