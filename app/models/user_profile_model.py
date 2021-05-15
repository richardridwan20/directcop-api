from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from config.database import Base


class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(String(50), primary_key=True, index=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    address = Column(String(200))
    postal_code = Column(String(100))
    city = Column(String(100))
    phone_number = Column(String(100))
    email = Column(String(100))
    is_active = Column(Boolean())
    user_id = Column(String(100))
    provider_id = Column(String(100))