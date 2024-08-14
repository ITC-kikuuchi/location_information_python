from fastapi import FastAPI

import logging

# ロギングの設定
logging.basicConfig(
    filename="app.log", level=logging.DEBUG, format="%(asctime)s %(message)s"
)

from routers import Area, Attendance, Auth, User, UserLocation, UserStatus

app = FastAPI()
app.include_router(Area.router)
app.include_router(Attendance.router)
app.include_router(Auth.router)
app.include_router(User.router)
app.include_router(UserLocation.router)
app.include_router(UserStatus.router)