from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from routers.Auth import getCurrentUser

import cruds.User as UserCrud
import schemas.User as UserSchema

router = APIRouter()


# ユーザ一覧取得API
@router.get("/users", response_model=list[UserSchema.getUsers])
def getUsers(loginUser: dict = Depends(getCurrentUser), db: Session = Depends(get_db)):
    try:
        # 権限チェック
        if not loginUser.is_admin:
            # 管理者権限が存在しない場合
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden"
            )
        # ユーザ一覧取得
        Users = UserCrud.getUsers(db)
        return Users
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ユーザ登録API
@router.post("/users")
def createUser(
    item: UserSchema.createUser,
    loginUser: dict = Depends(getCurrentUser),
    db: Session = Depends(get_db),
):
    try:
        # 権限チェック
        if not loginUser.is_admin:
            # 管理者権限が存在しない場合
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden"
            )
        # 登録データの作成
        user = {
            "user_name": item.user_name,
            "user_name_kana": item.user_name_kana,
            "mail_address": item.mail_address,
            "password": item.password,
            "is_admin": item.is_admin,
            "default_area_id": item.default_area_id,
        }
        # ユーザデータ登録処理
        UserCrud.createUser(db, user, loginUser)
        return
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ユーザ詳細取得API
@router.get("/users/{user_id}", response_model=UserSchema.getUserDetail)
def getUserDetail(
    user_id: int,
    loginUser: dict = Depends(getCurrentUser),
    db: Session = Depends(get_db),
):
    try:
        # ユーザID に紐づくデータの取得
        user = UserCrud.getUserDetail(db, userId=user_id)
        if not user:
            # id に紐づくデータが存在しなかった場合
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="NotFound"
            )
        return user
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ユーザ更新API
@router.put("/users/{users_id}")
def updateUser():
    pass


# ユーザ削除API
@router.delete("/users/{users_id}")
def deleteUser():
    pass
