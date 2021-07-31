from sqlalchemy import Boolean, Column, String, DateTime
from sqlalchemy.orm import relationship

from config.database import Base


class UserCreate(Base):
    __tablename__ = "users"

    id = Column(String(50), primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True)
    full_name = Column(String(100))
    hashed_password = Column(String(100))
    is_active = Column(Boolean, default=True)
    
class User(UserCreate):
    extend_existing = True
    
    created_at = Column(DateTime()) 
    updated_at = Column(DateTime())