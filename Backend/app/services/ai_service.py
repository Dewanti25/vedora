from typing import List, Dict, Any
from datetime import datetime


async def answer_student_doubt(prompt: str, user: Dict[str, Any] = None, context: Dict[str, Any] = None) -> Dict[str, Any]:
    # Dummy response — replace with LLM integration later
    return {
        'answer': f"I can help with that: (stub reply) — received prompt: {prompt}",
        'confidence': 0.75,
        'timestamp': datetime.utcnow().isoformat(),
    }


async def generate_syllabus_plan(course_chapters: List[Dict[str, Any]], params: Dict[str, Any]) -> Dict[str, Any]:
    # Return a dummy syllabus plan based on chapters
    weeks = params.get('weeks', 8)
    plan = []
    per_week = max(1, len(course_chapters) // weeks) if weeks else 1
    idx = 0
    for w in range(weeks):
        assignments = []
        for _ in range(per_week):
            if idx < len(course_chapters):
                assignments.append({'chapter': course_chapters[idx].get('title', f'Chapter {idx+1}')})
                idx += 1
        plan.append({'week': w+1, 'assignments': assignments})
    return {'weeklyPlan': plan, 'generatedBy': 'AI', 'generatedAt': datetime.utcnow().isoformat()}


async def generate_homework(chapters: List[Dict[str, Any]], params: Dict[str, Any]) -> List[Dict[str, Any]]:
    # Produce 1 dummy homework per chapter slice
    hw = []
    for i, ch in enumerate(chapters[:5]):
        hw.append({'title': f'Homework {i+1}: {ch.get("title")}', 'description': f'Practice problems from {ch.get("title")}', 'dueDays': 7})
    return hw


async def evaluate_homework(submission: Dict[str, Any]) -> Dict[str, Any]:
    # Dummy evaluation: give full marks if submission has file, else 0
    has_file = bool(submission.get('fileUrl'))
    marks = submission.get('maxMarks', 10) if has_file else 0
    feedback = 'Good work' if has_file else 'No submission found'
    return {'marks': marks, 'feedback': feedback, 'evaluatedAt': datetime.utcnow().isoformat()}


async def generate_quiz(chapters: List[Dict[str, Any]], params: Dict[str, Any]) -> Dict[str, Any]:
    # Create a 5-question dummy quiz
    questions = []
    for i in range(5):
        questions.append({'question': f'Dummy Q{i+1} about {chapters[i%len(chapters)].get("title","topic")}', 'options': ['A','B','C','D'], 'correctAnswer': 'A', 'marks': 1})
    return {'title': params.get('title','Auto Quiz'), 'questions': questions, 'durationMinutes': params.get('durationMinutes', 20)}


async def detect_weak_topics(student_history: Dict[str, Any]) -> List[str]:
    # Simple heuristic stub: return two topics
    return ['Fractions', 'Algebra Basics']


async def generate_session_summary(messages: List[Dict[str, Any]]) -> Dict[str, Any]:
    # Return a short dummy summary
    summary = 'This session covered key points and assigned follow-ups.'
    return {'summary': summary, 'generatedAt': datetime.utcnow().isoformat()}
async def generate_syllabus_from_textbook(textbook_id: str):
    # placeholder that would call an LLM or pipeline
    return {'plan_id': 'demo-plan'}
