from sqlalchemy import Boolean, Column, String, DateTime
from sqlalchemy.orm import relationship

from config.database import Base


class UserLicenseCreate(Base):
    __tablename__ = "user_licenses"

    id = Column(String(50), primary_key=True, index=True)
    user_id = Column(String(100))
    license_type = Column(String(100))
    status = Column(String(100))
    start_date = Column(String(100))
    end_date = Column(String(100))

class UserLicense(UserLicenseCreate):
    extend_existing = True
    
    created_at = Column(DateTime()) 
    updated_at = Column(DateTime())
