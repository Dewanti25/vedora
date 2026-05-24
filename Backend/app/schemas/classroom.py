from pydantic import BaseModel
from typing import Optional

class ClassroomCreate(BaseModel):
    board: str
    class_grade: str
    subject: str
    title: str
    fileName: Optional[str]
