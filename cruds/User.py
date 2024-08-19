from sqlalchemy.orm import Session

import models.m_user as UserModel


# ユーザ一覧取得
def getUsers(db: Session):
    return db.query(UserModel.User).all()
