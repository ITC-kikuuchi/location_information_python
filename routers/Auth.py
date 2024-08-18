from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from datetime import datetime, timedelta
from jose import jwt, JWTError

import os
import cruds.Auth as AuthCrud
import schemas.Auth as AuthSchema

router = APIRouter()


# トークン生成処理
def createTokens(user_id: int):
    # ペイロード生成
    accessPayload = {
        "token_type": "access_token",
        "exp": datetime.utcnow() + timedelta(minutes=60),
        "user_id": user_id,
    }
    # アクセストークンの生成
    accessToken = jwt.encode(
        accessPayload, os.environ["SECRET_KEY"], algorithm="HS256"
    )
    # アクセストークンの返却
    return {"access_token": accessToken, "token_type": "bearer"}


# ログインAPI
@router.post("/login")
async def login(
    formData: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    # 入力された情報に紐づくユーザデータの取得
    user = AuthCrud.getUser(db, mail=formData.username, password=formData.password)
    if not user:
        # 入力された情報に紐づくユーザデータが存在しない場合
        raise HTTPException(
            # 401 エラーの返却
            status_code=401,
            detail=f"メールアドレスまたはパスワードが違います。",
        )
    # トークン生成し返却
    return createTokens(user.id)


# ログイン情報取得API
@router.post("/me")
def me():
    pass


# ログアウトAPI
@router.get("/logout")
def logout():
    pass
