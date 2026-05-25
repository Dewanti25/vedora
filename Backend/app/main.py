from fastapi import FastAPI, Depends, HTTPException, status, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import bcrypt
import hashlib
from jose import JWTError, jwt
from pymongo import MongoClient
import certifi
import logging
from dotenv import load_dotenv
import os
from typing import Optional
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
JWT_SECRET = os.getenv("JWT_SECRET", "change-me")
ALGORITHM = "HS256"
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")
DB_NAME = os.getenv("MONGODB_DB", "Vedora")


try:
    # Use certifi CA bundle to avoid TLS handshake issues on some hosts
    client = MongoClient(
        MONGODB_URI,
        tls=True,
        tlsCAFile=certifi.where(),
        serverSelectionTimeoutMS=30000,
        connectTimeoutMS=20000,
    )
    # Use DB name from env (default 'Vedora') to avoid casing conflicts
    db = client.get_database(DB_NAME)
    # verify connection
    client.admin.command('ping')
    logger.info("Connected to MongoDB (ping successful)")
except Exception:
    logger.exception("Failed to connect to MongoDB at startup")
    # keep going; operations will raise on DB use and be logged
    client = MongoClient(MONGODB_URI)
    db = client.get_database(DB_NAME)

app = FastAPI(title="Vedora AI - Backend")

logger = logging.getLogger("vedora.main")
logging.basicConfig(level=logging.INFO)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL, "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserCreate(BaseModel):
    email: str
    password: str
    role: Optional[str] = "student"


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


def _pre_hash_if_needed(password: str) -> bytes:
    b = password.encode("utf-8")
    if len(b) > 72:
        return hashlib.sha256(b).hexdigest().encode("utf-8")
    return b


def hash_password(password: str) -> str:
    key = _pre_hash_if_needed(password)
    hashed = bcrypt.hashpw(key, bcrypt.gensalt())
    return hashed.decode('utf-8')


def verify_password(plain: str, hashed: str) -> bool:
    key = _pre_hash_if_needed(plain)
    try:
        return bcrypt.checkpw(key, hashed.encode('utf-8'))
    except ValueError:
        return False


def create_access_token(data: dict) -> str:
    return jwt.encode(data, JWT_SECRET, algorithm=ALGORITHM)


def get_user_by_email(email: str):
    try:
        return db.users.find_one({"email": email})
    except Exception:
        logger.exception("Error querying user by email")
        return None


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if not credentials or not credentials.credentials:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    token = credentials.credentials
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    user = get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    user["id"] = str(user.get("_id"))
    return user


@app.post("/register", response_model=dict)
def register(u: UserCreate):
    try:
        if get_user_by_email(u.email):
            raise HTTPException(status_code=400, detail="User already exists")
        user = {"email": u.email, "password": hash_password(u.password), "role": u.role}
        db.users.insert_one(user)
        return {"msg": "registered", "email": user["email"]}
    except HTTPException:
        raise
    except Exception:
        logger.exception("Failed to register user")
        raise HTTPException(status_code=500, detail="Internal server error")


@app.post("/login", response_model=Token)
def login(u: UserCreate):
    try:
        user = get_user_by_email(u.email)
        if not user or not verify_password(u.password, user.get("password", "")):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        token = create_access_token({"sub": user["email"]})
        return {"access_token": token, "token_type": "bearer"}
    except HTTPException:
        raise
    except Exception:
        logger.exception("Login failed")
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/me")
def me(user=Depends(get_current_user)):
    return {"email": user["email"], "role": user.get("role", "student")}


@app.post("/upload")
def upload_file(file: UploadFile = File(...), user=Depends(get_current_user)):
    uploads_dir = os.path.join(os.path.dirname(__file__), "uploads")
    os.makedirs(uploads_dir, exist_ok=True)
    filepath = os.path.join(uploads_dir, file.filename)
    with open(filepath, "wb") as f:
        f.write(file.file.read())
    db.files.insert_one({"filename": file.filename, "owner": user["email"]})
    return {"filename": file.filename}


@app.get("/courses")
def list_courses():
    items = list(db.courses.find({}, {"_id": 0}))
    return {"courses": items}


@app.get("/stats")
def stats(credentials: Optional[HTTPAuthorizationCredentials] = Depends(security)):
    # Basic aggregated stats to drive the dashboard widgets
    courses_count = db.courses.count_documents({})
    files_count = db.files.count_documents({}) if 'files' in db.list_collection_names() else 0

    # Try to surface user-specific progress if a valid token is provided; fall back to defaults
    user_doc = None
    if credentials and credentials.credentials:
        try:
            payload = jwt.decode(credentials.credentials, JWT_SECRET, algorithms=[ALGORITHM])
            email = payload.get("sub")
            if email:
                user_doc = get_user_by_email(email)
        except JWTError:
            user_doc = None
    overall_progress = user_doc.get("progress", 75) if user_doc else 75
    study_time_hours = user_doc.get("study_time_hours", 24.6) if user_doc else 24.6
    concepts_learned = user_doc.get("concepts_learned", 128) if user_doc else 128

    # Sample subject progress
    subject_progress = [
        {"name": "Mathematics", "percent": user_doc.get("math", 85) if user_doc else 85},
        {"name": "Physics", "percent": user_doc.get("physics", 70) if user_doc else 70},
    ]

    performance = {"easy": 85, "medium": 72, "hard": 58}

    return {
        "courses_count": courses_count,
        "files_count": files_count,
        "overall_progress": overall_progress,
        "study_time_hours": study_time_hours,
        "concepts_learned": concepts_learned,
        "subject_progress": subject_progress,
        "performance": performance,
    }


@app.post("/courses")
def create_course(payload: dict, user=Depends(get_current_user)):
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin only")
    db.courses.insert_one(payload)
    return {"msg": "created"}


if __name__ == "__main__":
    import uvicorn
    # Run with reload watching only the Backend folder to avoid reload loops
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, reload_dirs=["Backend"]) 
