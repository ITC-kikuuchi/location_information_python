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

# OAuth2PasswordBearerを使用してトークン取得用エンドポイントを設定
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# トークン生成処理
def createTokens(user_id: int):
    # ペイロード生成
    accessPayload = {
        "token_type": "access_token",
        "exp": datetime.utcnow() + timedelta(minutes=60),
        "user_id": user_id,
    }
    # アクセストークンの生成
    accessToken = jwt.encode(accessPayload, os.environ["SECRET_KEY"], algorithm="HS256")
    # アクセストークンの返却
    return {"access_token": accessToken, "token_type": "bearer"}


# トークンを検証してユーザーを取得
def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    # エラーメッセージの作成
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Unauthorized",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # トークンをデコードしてペイロードを取得
        payload = jwt.decode(token, os.environ["SECRET_KEY"], algorithms=["HS256"])
        # ID に紐づくユーザ情報の取得
        user = AuthCrud.getUserById(db, payload["user_id"])
        if not user:
            # ID に紐づくユーザ情報が取得できなかった場合
            raise credentials_exception
        # ログインユーザ取得API の場合
        return user
    except JWTError:
        # jwt でエラーが発生した場合
        raise credentials_exception


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
