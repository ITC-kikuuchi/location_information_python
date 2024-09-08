from sqlalchemy.orm import Session

import models.m_attendance as AttendanceModel


# 勤怠状況一覧取得
def getAttendances(db: Session):
    return db.query(AttendanceModel.Attendance).all()
