from typing import Optional, List
from pydantic import BaseModel
from .general_schema import Meta

class UserLicenseBase(BaseModel):
    license_type: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    user_id: Optional[str]


class UserLicenseId(BaseModel):
    id: str


class UserLicenseCreate(UserLicenseBase):
    pass

class UserLicenseUpdate(BaseModel):
    license_type: str
    start_date: str
    end_date: str
    user_id: str
    pass


class UserLicense(UserLicenseBase):
    id: str
    status: Optional[str]

    class Config:
        orm_mode = True
        
class UserLicensePaginate(BaseModel):
    data: List[UserLicense]
    meta: Meta
