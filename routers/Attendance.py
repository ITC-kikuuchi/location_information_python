from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict
from database import get_db
from routers.Auth import getCurrentUser


import cruds.Attendance as AttendanceCrud
import schemas.Attendance as AttendanceSchema

router = APIRouter()


# 勤務状況一覧取得API
@router.get(
    "/attendances", response_model=Dict[str, list[AttendanceSchema.getAttendances]]
)
def getAttendances(
    loginUser: dict = Depends(getCurrentUser), db: Session = Depends(get_db)
):
    try:
        # 勤怠状況一覧取得
        attendances = {"attendance_list": AttendanceCrud.getAttendances(db)}
        # OK レスポンス
        return attendances
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
