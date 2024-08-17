from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from datetime import datetime, timedelta
from jose import jwt

import os
import cruds.Auth as AuthCrud

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
def login():
    pass

# ログイン情報取得API
@router.post("/me")
def me():
    pass

# ログアウトAPI
@router.get("/logout")
def logout():
    pass