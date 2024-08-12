from fastapi import FastAPI

import logging

# ロギングの設定
logging.basicConfig(
    filename="app.log", level=logging.DEBUG, format="%(asctime)s %(message)s"
)

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "world"}