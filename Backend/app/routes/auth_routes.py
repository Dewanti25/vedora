from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from ..services.user_service import get_user_by_email, create_user
from ..services.password_service import hash_password, verify_password
from ..security import create_access_token
from ..deps import get_current_user
from typing import Optional
from datetime import timedelta

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



@router.post('/demo-token')
async def demo_token():
    """Return a short-lived demo token for guest/demo access.

    This token should only grant a guest role and must be short-lived.
    """
    token = create_access_token('guest@vedora.local', expires_delta=timedelta(hours=1))
    return {'token': token, 'user': {'id': 'guest', 'email': 'guest@vedora.local', 'name': 'Demo User', 'role': 'guest'}}
