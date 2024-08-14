from fastapi import APIRouter

router = APIRouter()

# ログインAPI
@router.post("/login")
def login():
    pass

# ログイン情報詳細取得API
@router.post("/me")
def me():
    pass

# ログアウトAPI
@router.get("/logout")
def logout():
    pass