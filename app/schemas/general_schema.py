from pydantic import BaseModel
from typing import Optional


class Delete(BaseModel):
    message: Optional[str] = "Deleted successfully"
    id: str

    class Config:
        orm_mode = True


class Validation(BaseModel):
    loc: Optional[str]
    msg: Optional[str]
    type: Optional[str]

    class Config:
        orm_mode = True

class Meta(BaseModel):
    page_size: int
    page_number: int
    num_pages: int
    total_results: int
