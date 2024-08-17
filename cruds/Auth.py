from sqlalchemy.orm import Session

import models.m_user as UserModel


# ユーザ取得
def getUser(db: Session, mail: str, password: str):
    return (
        db.query(UserModel.User)
        .filter(
            UserModel.User.mail_address == mail,
            UserModel.User.password == password,
        )
        .first()
    )
