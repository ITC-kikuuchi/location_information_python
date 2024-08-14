from fastapi import APIRouter

router = APIRouter()

# ユーザステータス一覧取得API
@router.post("/user-status")
def getUserStatus():
    pass