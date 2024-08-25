from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from routers.Auth import getCurrentUser

import cruds.User as UserCrud
import schemas.User as UserSchema

router = APIRouter()

# 管理者権限及びIDチェック
def CheckExecutionAuthority(loginUser, user_id = None):
    # 権限チェック
    if not loginUser.is_admin:
        # 管理者権限が存在しない場合
        if not user_id or loginUser.id != user_id:
            # ユーザID が存在しない、またはログインユーザのID と一致しない場合
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden"
            )

# ユーザ一覧取得API
@router.get("/users", response_model=list[UserSchema.getUsers])
def getUsers(loginUser: dict = Depends(getCurrentUser), db: Session = Depends(get_db)):
    try:
        # 権限チェック
        CheckExecutionAuthority(loginUser)
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
        CheckExecutionAuthority(loginUser)
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
        return {"message": "Operation completed successfully"}
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
        # 権限チェック
        CheckExecutionAuthority(loginUser, user_id)
        # ユーザID に紐づくデータの取得
        user = UserCrud.getUserDetail(db, user_id)
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
@router.put("/users/{user_id}")
def updateUser(
    user_id: int,
    item: UserSchema.updateUser,
    loginUser: dict = Depends(getCurrentUser),
    db: Session = Depends(get_db),
):
    try:
        # 権限チェック
        CheckExecutionAuthority(loginUser, user_id)
        # ユーザID に紐づくデータの取得
        user = UserCrud.getUserDetail(db, user_id)
        if not user:
            # id に紐づくデータが存在しなかった場合
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="NotFound"
            )
        # 更新データの作成
        updateUser = {
            "user_name": item.user_name,
            "user_name_kana": item.user_name_kana,
            "mail_address": item.mail_address,
            "is_admin": item.is_admin,
            "default_area_id": item.default_area_id,
            "password": item.password if item.password else user.password
        }
        # ユーザデータ更新処理
        UserCrud.updateUser(db, updateUser, loginUser, user)
        return {"message": "Operation completed successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ユーザ削除API
@router.delete("/users/{users_id}")
def deleteUser():
    pass
