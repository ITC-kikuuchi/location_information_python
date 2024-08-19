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