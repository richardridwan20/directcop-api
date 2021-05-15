from typing import Optional
from pydantic import BaseModel


class UserProfileBase(BaseModel):
    user_id: str
    provider_id: str
    first_name: str
    last_name: str
    address: str
    postal_code: str
    city: str
    phone_number: str
    email: str
    is_active: bool


class UserProfileId(BaseModel):
    id: str


class UserProfileCreate(UserProfileBase):
    pass

class UserProfileUpdate(UserProfileBase):
    pass


class UserProfile(UserProfileBase):
    id: str

    class Config:
        orm_mode = True
