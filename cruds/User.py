from sqlalchemy.orm import Session

import models.m_user as UserModel


# ユーザ一覧取得
def getUsers(db: Session):
    return db.query(UserModel.User).all()

# ユーザ登録
def createUser(db: Session, user, loginUser):
    createUser = UserModel.User(
        **user,
        created_id=loginUser.id,
        updated_id=loginUser.id
    )
    db.add(createUser)
    db.commit()
    db.refresh(createUser)