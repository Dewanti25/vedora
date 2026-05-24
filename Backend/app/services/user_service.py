from typing import Optional
from ..database import db
from bson import ObjectId


async def get_user_by_id(user_id: str) -> Optional[dict]:
    if db is None:
        return None
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        return None
    user["id"] = str(user.get("_id"))
    return user


async def get_user_by_email(email: str) -> Optional[dict]:
    if db is None:
        return None
    user = await db.users.find_one({"email": email})
    if not user:
        return None
    user["id"] = str(user.get("_id"))
    return user


async def create_user(user_data: dict) -> dict:
    if db is None:
        raise RuntimeError("Database not initialized")
    res = await db.users.insert_one(user_data)
    user = await db.users.find_one({"_id": res.inserted_id})
    user["id"] = str(user.get("_id"))
    return user
