from fastapi import APIRouter

router = APIRouter()

# ユーザステータス一覧取得API
@router.get("/user-status")
def getUserStatus():
    pass