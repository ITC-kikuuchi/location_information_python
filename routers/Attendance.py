from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict
from database import get_db
from routers.Auth import getCurrentUser


import cruds.Attendance as AttendanceCrud
import schemas.Attendance as AttendanceSchema

router = APIRouter()

# 勤務状況一覧取得API
@router.get("/attendances")
def getAttendances():
    pass