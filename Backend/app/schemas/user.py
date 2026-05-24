from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    name: Optional[str] = None
    email: EmailStr
    role: str = "student"
    profileImage: Optional[str] = None


class UserInDB(UserBase):
    id: str = Field(..., alias="_id")
    createdAt: datetime


class UserOut(UserBase):
    id: str
    createdAt: datetime

    class Config:
        orm_mode = True
