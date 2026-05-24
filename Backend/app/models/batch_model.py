from typing import List

def batch_document(name: str, board: str, class_grade: str, subject: str, max_students: int = 15) -> dict:
    return {
        'name': name,
        'board': board,
        'class': class_grade,
        'subject': subject,
        'max': max_students,
        'students': 0,
        'createdAt': None,
    }
