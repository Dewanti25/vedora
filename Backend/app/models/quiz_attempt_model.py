from datetime import datetime
from typing import List, Optional


def quiz_attempt_document(
    quizId: str,
    studentId: str,
    answers: List[dict],
    score: float,
    percentage: float,
):
    return {
        'quizId': quizId,
        'studentId': studentId,
        'answers': answers,
        'score': score,
        'percentage': percentage,
        'submittedAt': datetime.utcnow(),
    }
def quiz_attempt_document(quiz_id: str, user_id: str, score: float):
    return {'quiz_id': quiz_id, 'user_id': user_id, 'score': score, 'createdAt': None}
