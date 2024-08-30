from sqlalchemy.orm import Session

import models.m_area as AreaModel


# エリア一覧取得
def getAreas(db: Session):
    return db.query(AreaModel.Area).all()