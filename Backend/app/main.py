from fastapi import FastAPI, Depends, HTTPException, status, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import Optional
from jose import JWTError, jwt
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import bcrypt
import hashlib
import certifi
import logging
import os
from dotenv import load_dotenv

load_dotenv()

# --------------------------------------------------
# Environment variables
# --------------------------------------------------

MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DB = os.getenv("MONGODB_DB", "Vedora")
JWT_SECRET = os.getenv("JWT_SECRET", "change-me")
ALGORITHM = "HS256"
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")

if not MONGODB_URI:
    raise RuntimeError("MONGODB_URI is not set")

# --------------------------------------------------
# Logging
# --------------------------------------------------

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("vedora.main")

# --------------------------------------------------
# MongoDB connection
# --------------------------------------------------

client = MongoClient(
    MONGODB_URI,
    tls=True,
    tlsCAFile=certifi.where(),
    server_api=ServerApi("1"),
    serverSelectionTimeoutMS=30000,
    connectTimeoutMS=20000,
)

db = client[MONGODB_DB]

# --------------------------------------------------
# FastAPI app
# --------------------------------------------------

app = FastAPI(title="Vedora AI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        FRONTEND_URL,
        "https://vedora-six.vercel.app",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBearer(auto_error=False)

# --------------------------------------------------
# Schemas
# --------------------------------------------------

class UserCreate(BaseModel):
    email: str
    password: str
    role: Optional[str] = "student"


class LoginRequest(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# --------------------------------------------------
# Helper functions
# --------------------------------------------------

def _pre_hash_if_needed(password: str) -> bytes:
    password_bytes = password.encode("utf-8")

    if len(password_bytes) > 72:
        return hashlib.sha256(password_bytes).hexdigest().encode("utf-8")

    return password_bytes


def hash_password(password: str) -> str:
    key = _pre_hash_if_needed(password)
    hashed = bcrypt.hashpw(key, bcrypt.gensalt())
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    key = _pre_hash_if_needed(plain_password)

    try:
        return bcrypt.checkpw(key, hashed_password.encode("utf-8"))
    except Exception:
        return False


def create_access_token(data: dict) -> str:
    return jwt.encode(data, JWT_SECRET, algorithm=ALGORITHM)


def serialize_user(user: dict) -> dict:
    return {
        "id": str(user.get("_id")),
        "email": user.get("email"),
        "role": user.get("role", "student"),
    }


def get_user_by_email(email: str):
    return db.users.find_one({"email": email})


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if not credentials or not credentials.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    token = credentials.credentials

    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        email = payload.get("sub")

        if not email:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
            )

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    user = get_user_by_email(email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    return user


# --------------------------------------------------
# Basic routes
# --------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "Vedora AI Backend is running",
        "docs": "/docs",
        "health": "/health",
        "db_test": "/db-test",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/db-test")
def db_test():
    try:
        client.admin.command("ping")
        return {
            "database": "connected",
            "db_name": MONGODB_DB,
        }
    except Exception as error:
        logger.exception("MongoDB ping failed")
        raise HTTPException(
            status_code=500,
            detail=f"MongoDB connection failed: {str(error)}",
        )


# --------------------------------------------------
# Auth routes
# --------------------------------------------------

@app.post("/register", response_model=dict)
def register(user_data: UserCreate):
    try:
        existing_user = get_user_by_email(user_data.email)

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="User already exists",
            )

        user = {
            "email": user_data.email,
            "password": hash_password(user_data.password),
            "role": user_data.role or "student",
        }

        result = db.users.insert_one(user)

        return {
            "msg": "registered",
            "user": {
                "id": str(result.inserted_id),
                "email": user["email"],
                "role": user["role"],
            },
        }

    except HTTPException:
        raise

    except Exception as error:
        logger.exception("Failed to register user")
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(error)}",
        )


@app.post("/login", response_model=Token)
def login(login_data: LoginRequest):
    try:
        user = get_user_by_email(login_data.email)

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials",
            )

        stored_password = user.get("password", "")

        if not verify_password(login_data.password, stored_password):
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials",
            )

        token = create_access_token(
            {
                "sub": user["email"],
                "role": user.get("role", "student"),
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }

    except HTTPException:
        raise

    except Exception as error:
        logger.exception("Login failed")
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(error)}",
        )


@app.get("/me")
def me(current_user=Depends(get_current_user)):
    return {
        "user": serialize_user(current_user),
    }


# --------------------------------------------------
# File upload route
# --------------------------------------------------

@app.post("/upload")
def upload_file(
    file: UploadFile = File(...),
    current_user=Depends(get_current_user),
):
    uploads_dir = os.path.join(os.path.dirname(__file__), "uploads")
    os.makedirs(uploads_dir, exist_ok=True)

    filepath = os.path.join(uploads_dir, file.filename)

    with open(filepath, "wb") as saved_file:
        saved_file.write(file.file.read())

    db.files.insert_one(
        {
            "filename": file.filename,
            "owner": current_user["email"],
        }
    )

    return {
        "filename": file.filename,
        "message": "File uploaded successfully",
    }


# --------------------------------------------------
# Course routes
# --------------------------------------------------

@app.get("/courses")
def list_courses():
    courses = list(db.courses.find({}, {"_id": 0}))
    return {"courses": courses}


@app.post("/courses")
def create_course(payload: dict, current_user=Depends(get_current_user)):
    if current_user.get("role") != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin only",
        )

    db.courses.insert_one(payload)

    return {
        "msg": "created",
    }


# --------------------------------------------------
# Dashboard stats route
# --------------------------------------------------

@app.get("/stats")
def stats(credentials: Optional[HTTPAuthorizationCredentials] = Depends(security)):
    courses_count = db.courses.count_documents({})

    files_count = 0
    if "files" in db.list_collection_names():
        files_count = db.files.count_documents({})

    user_doc = None

    if credentials and credentials.credentials:
        try:
            payload = jwt.decode(
                credentials.credentials,
                JWT_SECRET,
                algorithms=[ALGORITHM],
            )
            email = payload.get("sub")

            if email:
                user_doc = get_user_by_email(email)

        except JWTError:
            user_doc = None

    overall_progress = user_doc.get("progress", 75) if user_doc else 75
    study_time_hours = user_doc.get("study_time_hours", 24.6) if user_doc else 24.6
    concepts_learned = user_doc.get("concepts_learned", 128) if user_doc else 128

    subject_progress = [
        {
            "name": "Mathematics",
            "percent": user_doc.get("math", 85) if user_doc else 85,
        },
        {
            "name": "Physics",
            "percent": user_doc.get("physics", 70) if user_doc else 70,
        },
    ]

    performance = {
        "easy": 85,
        "medium": 72,
        "hard": 58,
    }

    return {
        "courses_count": courses_count,
        "files_count": files_count,
        "overall_progress": overall_progress,
        "study_time_hours": study_time_hours,
        "concepts_learned": concepts_learned,
        "subject_progress": subject_progress,
        "performance": performance,
    }


# --------------------------------------------------
# Local development only
# --------------------------------------------------

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
