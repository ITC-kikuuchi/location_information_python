from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.orm import relationship

from database import Base


class Attendance(Base):
    __tablename__ = "m_attendance"

    id = Column(Integer, primary_key=True, nullable=False)
    attendance_status = Column(String(255), nullable=False)
    created_id = Column(Integer)
    updated_id = Column(Integer)
    created_at = Column(Timestamp)
    updated_at = Column(Timestamp)
    
    user = relationship("User", back_populates="attendance")
