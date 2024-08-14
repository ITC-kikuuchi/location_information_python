from fastapi import APIRouter

router = APIRouter()

# ユーザ位置情報一覧取得API
@router.post("/user-locations")
def getUsers():
    pass

# ユーザ位置情報詳細取得API
@router.get("/user-locations/{user_id}")
def getUserDetail():
    pass

# ユーザ位置情報更新API
@router.put("/user-locations/{users_id}")
def updateUser():
    pass
