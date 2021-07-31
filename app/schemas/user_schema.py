from typing import Optional, List
from .general_schema import Meta
from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    is_active: Optional[bool] = 1

    class Config:
        orm_mode = True


class UserId(BaseModel):
    id: str


class UserInDB(User):
    hashed_password: str

class UserPaginate(BaseModel):
    data: List[User]
    meta: Meta