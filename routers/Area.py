from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict
from database import get_db
from routers.Auth import getCurrentUser


import cruds.Area as AreaCrud
import schemas.Area as AreaSchema

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


# エリア一覧取得API
@router.get("/areas", response_model=Dict[str, list[AreaSchema.getAreas]])
def getAreas(loginUser: dict = Depends(getCurrentUser), db: Session = Depends(get_db)):
    try:
        # エリア一覧取得
        areas = {'area_list': AreaCrud.getAreas(db)}
        # OK レスポンス
        return areas
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# エリア登録API
@router.post("/areas")
def createArea():
    pass

# エリア詳細取得API
@router.get("/areas/{area_id}")
def getAreaDetail():
    pass

# エリア更新API
@router.put("/areas/{area_id}")
def updateArea():
    pass

# エリア削除API
@router.delete("/areas/{area_id}")
def deleteArea():
    pass