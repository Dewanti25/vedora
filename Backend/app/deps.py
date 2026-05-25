from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .services.auth_service import verify_token
from .services.user_service import get_user_by_email
import os

security = HTTPBearer()


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    allow_anonymous = os.getenv("ALLOW_ANONYMOUS", "true").lower() in ("1", "true", "yes")

    # If no credentials were provided, either return a guest user (when allowed)
    # or raise an authentication error.
    if not credentials or not credentials.credentials:
        if allow_anonymous:
            return {"id": "guest", "email": "guest@vedora.local", "role": "guest"}
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

    token = credentials.credentials
    try:
        payload = verify_token(token)
    except Exception:
        if allow_anonymous:
            return {"id": "guest", "email": "guest@vedora.local", "role": "guest"}
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    # token subject may be user id or email
    email = payload.get("sub") or payload.get("email")
    if not email:
        if allow_anonymous:
            return {"id": "guest", "email": "guest@vedora.local", "role": "guest"}
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")

    # try by email then by id
    try:
        user = await get_user_by_email(email)
    except Exception:
        user = None

    if not user:
        if allow_anonymous:
            return {"id": "guest", "email": "guest@vedora.local", "role": "guest"}
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user


async def admin_required(user=Depends(get_current_user)):
    if user.get("role") != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required")
    return user


async def student_required(user=Depends(get_current_user)):
    if user.get("role") != "student":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Student access required")
    return user


async def teacher_required(user=Depends(get_current_user)):
    if user.get("role") != "teacher":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Teacher access required")
    return user


async def get_optional_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Return a user when a valid token is provided, otherwise return None.

    Use this dependency for routes that should allow both authenticated and
    unauthenticated (guest) access.
    """
    if not credentials or not credentials.credentials:
        return None
    token = credentials.credentials
    try:
        payload = verify_token(token)
    except Exception:
        return None

    email = payload.get("sub") or payload.get("email")
    if not email:
        return None
    try:
        user = await get_user_by_email(email)
    except Exception:
        user = None
    return user
