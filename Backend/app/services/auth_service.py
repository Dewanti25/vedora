from datetime import datetime, timedelta

async def authenticate(email: str, password: str):
    # placeholder authentication
    if email and password:
        return {'email': email, 'token': 'demo-token'}
    return None
from jose import jwt, JWTError
from datetime import datetime, timedelta
from ..config import JWT_SECRET

ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: int = 60*24) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)


def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        raise
