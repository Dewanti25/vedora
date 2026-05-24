from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum


class Role(str, Enum):
    ADMIN = 'ADMIN'
    SCHOOL_ADMIN = 'SCHOOL_ADMIN'
    TEACHER = 'TEACHER'
    STUDENT = 'STUDENT'
    AI_ENGINE_MANAGER = 'AI_ENGINE_MANAGER'


class UserCreate(BaseModel):
    name: Optional[str]
    email: EmailStr
    password: str
    role: Optional[Role] = Role.STUDENT


class UserOut(BaseModel):
    id: str
    name: Optional[str]
    email: EmailStr
    role: Role
    schoolId: Optional[str]
    board: Optional[str]
    grade: Optional[str]
    profileImage: Optional[str]
    isActive: bool
    createdAt: Optional[str]
    updatedAt: Optional[str]
