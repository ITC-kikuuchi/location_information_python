from sqlalchemy.orm import Session

import models.m_area as AreaModel


# エリア一覧取得
def getAreas(db: Session):
    return db.query(AreaModel.Area).all()


# エリア登録
def createArea(db: Session, area, loginUser):
    createArea = AreaModel.Area(
        **area, created_id=loginUser.id, updated_id=loginUser.id
    )
    db.add(createArea)
    db.commit()
    db.refresh(createArea)


# エリア詳細取得
def getAreaDetail(db: Session, areaId: int):
    return db.query(AreaModel.Area).filter(AreaModel.Area.id == areaId).first()


# エリア更新
def updateArea(db: Session, area, loginUser, original: AreaModel.Area):
    for field, value in area.items():
        setattr(original, field, value)

    original.update_id = loginUser.id
    db.commit()
