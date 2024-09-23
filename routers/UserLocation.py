from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict
from database import get_db
from routers.Auth import getCurrentUser

import cruds.UserLocation as UserLocationCrud
import schemas.UserLocation as UserLocationSchema

router = APIRouter()


# ユーザ位置情報一覧取得API
@router.get(
    "/user-locations",
    response_model=Dict[str, list[UserLocationSchema.getUserLocations]],
)
def getUsers(loginUser: dict = Depends(getCurrentUser), db: Session = Depends(get_db)):
    # 初期値の設定
    transformed_users = []
    try:
        # ユーザ一覧取得
        Users = UserLocationCrud.getUserLocations(db)
        # レスポンスデータの作成
        for user in Users:
            transformed_user = UserLocationSchema.getUserLocations(
                id=user.id,
                user_name=user.user_name,
                user_name_kana=user.user_name_kana,
                area_id=user.area.id,
                area_name=user.area.area_name,
                attendance_id=user.attendance.id,
                attendance_status=user.attendance.attendance_status,
                status_id=user.user_status.id,
                user_status=user.user_status.user_status
            )
            transformed_users.append(transformed_user)
        # OK レスポンス
        return {"user_list": transformed_users}
    except HTTPException:
        raise
    except Exception as e:
        raise e


# ユーザ位置情報詳細取得API
@router.get("/user-locations/{user_id}")
def getUserDetail():
    pass


# ユーザ位置情報更新API
@router.put("/user-locations/{users_id}")
def updateUser():
    pass
