from datetime import datetime
from typing import List, Optional


def quiz_document(
    batchId: str,
    courseId: str,
    title: str,
    questions: List[dict],
    durationMinutes: int,
    createdBy: str,
    chapterId: Optional[str] = None,
):
    totalMarks = sum([q.get('marks', 0) for q in questions])
    return {
        'batchId': batchId,
        'courseId': courseId,
        'chapterId': chapterId,
        'title': title,
        'questions': questions,
        'totalMarks': totalMarks,
        'durationMinutes': durationMinutes,
        'createdBy': createdBy,
        'createdAt': datetime.utcnow(),
    }
def quiz_document(title: str, course_id: str):
    return {'title': title, 'course_id': course_id, 'createdAt': None}
