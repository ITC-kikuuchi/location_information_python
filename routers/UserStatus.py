from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict
from database import get_db
from routers.Auth import getCurrentUser


import cruds.UserStatus as UserStatusCrud
import schemas.UserStatus as UserStatusSchema

router = APIRouter()

# ユーザステータス一覧取得API
@router.get(
    "/user-status", response_model=Dict[str, list[UserStatusSchema.getUserStatus]]
)
def getUserStatus(
    loginUser: dict = Depends(getCurrentUser), db: Session = Depends(get_db)
):
    try:
        # ユーザステータス一覧取得
        user_status = {"user_status_list": UserStatusCrud.getUserStatus(db)}
        # OK レスポンス
        return user_status
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))