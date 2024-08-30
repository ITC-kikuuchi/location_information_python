from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict
from database import get_db
from routers.Auth import getCurrentUser


import cruds.Area as AreaCrud
import schemas.Area as AreaSchema

router = APIRouter()

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