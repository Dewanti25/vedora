from pydantic import BaseModel
from typing import List, Optional


class Question(BaseModel):
    question: str
    options: List[str]
    correctAnswer: str
    explanation: Optional[str] = None
    marks: int = 1


class QuizCreateRequest(BaseModel):
    batchId: str
    courseId: str
    chapterId: Optional[str] = None
    title: str
    questions: List[Question]
    durationMinutes: int


class QuizOut(BaseModel):
    id: str
    batchId: str
    courseId: str
    chapterId: Optional[str]
    title: str
    questions: List[dict]
    totalMarks: int
    durationMinutes: int
    createdBy: str
    createdAt: Optional[str]


class AttemptAnswer(BaseModel):
    questionIndex: int
    answer: str


class AttemptRequest(BaseModel):
    answers: List[AttemptAnswer]


class AttemptResult(BaseModel):
    attemptId: str
    score: float
    percentage: float
