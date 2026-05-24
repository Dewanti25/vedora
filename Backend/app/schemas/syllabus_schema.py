from pydantic import BaseModel
from typing import Optional, List


class SyllabusGenerateRequest(BaseModel):
    batchId: str
    courseId: str
    startDate: str
    endDate: str
    examDate: Optional[str] = None
    classesPerWeek: int = 3
    generatedBy: Optional[str] = 'AI'


class SyllabusOut(BaseModel):
    id: str
    batchId: str
    courseId: str
    startDate: str
    endDate: str
    examDate: Optional[str]
    classesPerWeek: int
    totalClasses: int
    revisionClasses: int
    testClasses: int
    weeklyPlan: List[dict]
    status: str
    generatedBy: str
    createdAt: Optional[str]
