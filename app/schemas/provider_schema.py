from typing import Optional
from pydantic import BaseModel


class ProviderBase(BaseModel):
    name: str
    slug: str
    url: str
    is_active: bool


class ProviderId(BaseModel):
    id: str


class ProviderCreate(ProviderBase):
    pass

class ProviderUpdate(ProviderBase):
    pass


class Provider(ProviderBase):
    id: str

    class Config:
        orm_mode = True
