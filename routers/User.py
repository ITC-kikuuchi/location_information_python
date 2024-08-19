from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from routers.Auth import getCurrentUser

import cruds.User as UserCrud
import schemas.User as UserSchema

router = APIRouter()

# ユーザ一覧取得API
@router.post("/users")
def getUsers():
    pass

# ユーザ登録API
@router.post("/users")
def createUser():
    pass

# ユーザ詳細取得API
@router.get("/users/{user_id}")
def getUserDetail():
    pass

# ユーザ更新API
@router.put("/users/{users_id}")
def updateUser():
    pass

# ユーザ削除API
@router.delete("/users/{users_id}")
def deleteUser():
    pass