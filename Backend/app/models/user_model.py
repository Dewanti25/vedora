from typing import Optional
from datetime import datetime


def user_document(
    email: str,
    name: str = '',
    passwordHash: str = '',
    role: str = 'STUDENT',
    schoolId: Optional[str] = None,
    board: Optional[str] = None,
    grade: Optional[str] = None,
    profileImage: Optional[str] = None,
    isActive: bool = True,
) -> dict:
    now = datetime.utcnow()
    return {
        'email': email,
        'name': name,
        'passwordHash': passwordHash,
        'role': role,
        'schoolId': schoolId,
        'board': board,
        'grade': grade,
        'profileImage': profileImage,
        'isActive': isActive,
        'createdAt': now,
        'updatedAt': now,
    }
