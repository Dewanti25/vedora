from pydantic import BaseModel, Field
from typing import Optional, List


class BatchCreate(BaseModel):
    board: str
    class_grade: str = Field(..., alias='class')
    subject: str
    name: str
    max_students: int = 15
    start_date: Optional[str]
    days: Optional[List[str]] = []
    start_time: Optional[str]
    end_time: Optional[str]


class BatchOut(BaseModel):
    id: str
    board: str
    class_grade: str
    subject: str
    name: str
    max_students: int
    students: int
    status: str
