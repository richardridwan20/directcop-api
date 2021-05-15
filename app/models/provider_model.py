from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from config.database import Base


class Provider(Base):
    __tablename__ = "providers"

    id = Column(String(50), primary_key=True, index=True)
    name = Column(String(100))
    slug = Column(String(100))
    url = Column(String(100))