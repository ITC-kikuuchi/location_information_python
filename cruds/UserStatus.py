from sqlalchemy.orm import Session

import models.m_user_status as UserStatusModel


# ユーザステータス一覧取得
def getUserStatus(db: Session):
    return db.query(UserStatusModel.UserStatus).all()
