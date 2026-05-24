from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from ..services.user_service import get_user_by_email, create_user
from ..services.password_service import hash_password, verify_password
from ..security import create_access_token
from ..deps import get_current_user
from typing import Optional

router = APIRouter(prefix="/auth", tags=["auth"])


class RegisterIn(BaseModel):
    name: Optional[str]
    email: EmailStr
    password: str
    role: Optional[str] = 'STUDENT'


class LoginIn(BaseModel):
    email: EmailStr
    password: str


@router.post('/register')
async def register(payload: RegisterIn):
    existing = await get_user_by_email(payload.email)
    if existing:
        raise HTTPException(status_code=400, detail='Email already registered')
    user_doc = {
        'name': payload.name,
        'email': payload.email,
        'passwordHash': hash_password(payload.password),
        'role': payload.role,
        'isActive': True,
        'createdAt': __import__('datetime').datetime.utcnow(),
        'updatedAt': __import__('datetime').datetime.utcnow()
    }
    user = await create_user(user_doc)
    token = create_access_token(str(user['id']))
    return {'token': token, 'user': {'id': user['id'], 'email': user['email'], 'name': user.get('name'), 'role': user.get('role')}}


@router.post('/login')
async def login(payload: LoginIn):
    user = await get_user_by_email(payload.email)
    if not user:
        raise HTTPException(status_code=400, detail='Invalid credentials')
    if not verify_password(payload.password, user.get('passwordHash')):
        raise HTTPException(status_code=400, detail='Invalid credentials')
    token = create_access_token(str(user['id']))
    return {'token': token, 'user': {'id': user['id'], 'email': user['email'], 'name': user.get('name'), 'role': user.get('role')}}


@router.get('/me')
async def me(user=Depends(get_current_user)):
    return {'id': user.get('id'), 'email': user.get('email'), 'name': user.get('name'), 'role': user.get('role')}
