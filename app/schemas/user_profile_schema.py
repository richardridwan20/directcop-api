from typing import Optional
from pydantic import BaseModel


class UserProfileBase(BaseModel):
    user_id: Optional[str]
    provider_id: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    address: Optional[str]
    postal_code: Optional[str]
    city: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]
    is_active: Optional[bool]
    card_name: Optional[str]
    card_number: Optional[str]
    card_expiry_date: Optional[str]
    card_cvv: Optional[str]
    address_2: Optional[str]
    address_3: Optional[str]
    profile_name: Optional[str]
    country: Optional[str]
    province: Optional[str]


class UserProfileId(BaseModel):
    id: str


class UserProfileCreate(BaseModel):
    provider_id: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    address: Optional[str]
    postal_code: Optional[str]
    city: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]
    is_active: Optional[bool] = True
    card_name: Optional[str]
    card_number: Optional[str]
    card_expiry_date: Optional[str]
    card_cvv: Optional[str]
    address_2: Optional[str]
    address_3: Optional[str]
    profile_name: Optional[str]
    country: Optional[str]
    province: Optional[str]
    pass

class UserProfileUpdate(UserProfileBase):
    pass


class UserProfile(UserProfileBase):
    id: str
    profile_name: str

    class Config:
        orm_mode = True
