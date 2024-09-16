from sqlalchemy.orm import Session, joinedload

import models.m_user as UserModel


# ユーザ位置情報一覧取得
def getUserLocations(db: Session):
    return (
        db.query(UserModel.User)
        .options(
            joinedload(UserModel.User.area),
            joinedload(UserModel.User.attendance),
        )
        .all()
    )
