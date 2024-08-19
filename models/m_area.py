from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.orm import relationship

from database import Base


class Area(Base):
    __tablename__ = "m_area"

    id = Column(Integer, primary_key=True, nullable=False)
    area_name = Column(String(255), nullable=False)
    is_default_area = Column(Boolean, nullable=False)
    created_id = Column(Integer)
    updated_id = Column(Integer)
    created_at = Column(Timestamp)
    updated_at = Column(Timestamp)

    user = relationship("User", back_populates="area")
