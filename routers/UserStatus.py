from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict
from database import get_db
from routers.Auth import getCurrentUser


import cruds.UserStatus as UserStatusCrud
import schemas.UserStatus as UserStatusSchema

router = APIRouter()

# ユーザステータス一覧取得API
@router.get("/user-status")
def getUserStatus():
    pass