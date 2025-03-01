from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict
from database import get_db
from routers.Auth import getCurrentUser


import cruds.Area as AreaCrud
import schemas.Area as AreaSchema

router = APIRouter()


# 管理者権限及びIDチェック
def CheckExecutionAuthority(loginUser, user_id=None):
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
        areas = {"area_list": AreaCrud.getAreas(db)}
        # OK レスポンス
        return areas
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# エリア登録API
@router.post("/areas")
def createArea(
    item: AreaSchema.createArea,
    loginUser: dict = Depends(getCurrentUser),
    db: Session = Depends(get_db),
):
    try:
        # 権限チェック
        CheckExecutionAuthority(loginUser)
        # 登録データの作成
        area = {
            "area_name": item.area_name,
            "is_default_area": item.is_default_area,
        }
        # ユーザデータ登録処理
        AreaCrud.createArea(db, area, loginUser)
        # OK レスポンス
        return {"message": "Operation completed successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# エリア詳細取得API
@router.get("/areas/{area_id}", response_model=AreaSchema.getAreaDetail)
def getAreaDetail(
    area_id: int,
    loginUser: dict = Depends(getCurrentUser),
    db: Session = Depends(get_db),
):
    try:
        # 権限チェック
        CheckExecutionAuthority(loginUser)
        # エリアID に紐づくデータの取得
        area = AreaCrud.getAreaDetail(db, area_id)
        if not area:
            # id に紐づくデータが存在しなかった場合
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="NotFound"
            )
        # OK レスポンス
        return area
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# エリア更新API
@router.put("/areas/{area_id}")
def updateArea(
    area_id: int,
    item: AreaSchema.updateArea,
    loginUser: dict = Depends(getCurrentUser),
    db: Session = Depends(get_db),
):
    try:
        # 権限チェック
        CheckExecutionAuthority(loginUser)
        # ユーザID に紐づくデータの取得
        area = AreaCrud.getAreaDetail(db, area_id)
        if not area:
            # id に紐づくデータが存在しなかった場合
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="NotFound"
            )
        # 更新データの作成
        updateArea = {
            "area_name": item.area_name,
            "is_default_area": item.is_default_area,
        }
        # ユーザデータ更新処理
        AreaCrud.updateArea(db, updateArea, loginUser, area)
        # OK レスポンス
        return {"message": "Operation completed successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# エリア削除API
@router.delete("/areas/{area_id}")
def deleteArea(
    area_id: int,
    loginUser: dict = Depends(getCurrentUser),
    db: Session = Depends(get_db),
):
    try:
        # 権限チェック
        CheckExecutionAuthority(loginUser)
        # エリアID に紐づくデータの取得
        area = AreaCrud.getAreaDetail(db, area_id)
        if not area:
            # id に紐づくデータが存在しなかった場合
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="NotFound"
            )
        # エリアデータ削除
        AreaCrud.deleteArea(db, area_id)
        # OK レスポンス
        return {"message": "Operation completed successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
