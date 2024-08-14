from fastapi import APIRouter

router = APIRouter()

# 勤務状況一覧取得API
@router.post("/attendances")
def getAttendances():
    pass