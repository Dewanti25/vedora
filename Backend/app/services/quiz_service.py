from datetime import datetime
from bson import ObjectId
from ..database import db
from ..models.quiz_model import quiz_document
from ..models.quiz_attempt_model import quiz_attempt_document


async def create_quiz(batchId: str, courseId: str, title: str, questions: list, durationMinutes: int, createdBy: str, chapterId: str = None):
    doc = quiz_document(batchId=batchId, courseId=courseId, title=title, questions=questions, durationMinutes=durationMinutes, createdBy=createdBy, chapterId=chapterId)
    res = await db.quizzes.insert_one(doc)
    return str(res.inserted_id)


async def list_quizzes():
    items = []
    cursor = db.quizzes.find({})
    async for q in cursor:
        q['id'] = str(q['_id'])
        items.append(q)
    return items


async def get_quiz(quizId: str):
    return await db.quizzes.find_one({'_id': ObjectId(quizId)})


async def submit_attempt(quizId: str, studentId: str, answers: list):
    # fetch quiz
    quiz = await db.quizzes.find_one({'_id': ObjectId(quizId)})
    if not quiz:
        return None
    questions = quiz.get('questions', [])
    totalMarks = quiz.get('totalMarks', 0) or sum([q.get('marks', 0) for q in questions])
    score = 0.0
    # answers expected as list with same order: [{'questionIndex': i, 'answer': '...'}]
    for a in answers:
        idx = a.get('questionIndex')
        ans = a.get('answer')
        if idx is None or idx < 0 or idx >= len(questions):
            continue
        q = questions[idx]
        correct = q.get('correctAnswer')
        if ans == correct:
            score += q.get('marks', 0)
    percentage = (score / totalMarks * 100) if totalMarks > 0 else 0.0
    attempt_doc = quiz_attempt_document(quizId=quizId, studentId=studentId, answers=answers, score=score, percentage=percentage)
    res = await db.quiz_attempts.insert_one(attempt_doc)
    return {'attemptId': str(res.inserted_id), 'score': score, 'percentage': percentage}


async def list_student_attempts(studentId: str):
    items = []
    cursor = db.quiz_attempts.find({'studentId': studentId})
    async for a in cursor:
        a['id'] = str(a['_id'])
        items.append(a)
    return items
