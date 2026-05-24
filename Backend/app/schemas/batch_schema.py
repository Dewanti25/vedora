from pydantic import BaseModel
from typing import Optional


class BatchCreate(BaseModel):
    name: str
    board: str
    class_grade: str
    subject: str
    max_students: Optional[int] = 15


class BatchOut(BaseModel):
    id: str
    name: str
    board: str
    class_grade: str
    subject: str
    max_students: int
