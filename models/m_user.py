from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp

from database import Base


class User(Base):
    __tablename__ = "m_user"

    id = Column(Integer, primary_key=True, nullable=False)
    mail_address = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    user_name = Column(String(255), nullable=False)
    user_name_kana = Column(String(255), nullable=False)
    default_area_id = Column(Integer, nullable=False)
    is_admin = Column(Boolean, nullable=False)
    area_id = Column(Integer, ForeignKey("m_area.id"), nullable=False)
    attendance_id = Column(Integer, ForeignKey("m_attendance.id"), nullable=False)
    user_status_id = Column(Integer, ForeignKey("m_user_status.id"), nullable=False)
    created_id = Column(Integer)
    updated_id = Column(Integer)
    created_at = Column(Timestamp)
    updated_at = Column(Timestamp)
