from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from datetime import datetime, timedelta
from jose import jwt

import os
import cruds.Auth as AuthCrud

router = APIRouter()

# ログインAPI
@router.post("/login")
def login():
    pass

# ログイン情報取得API
@router.post("/me")
def me():
    pass

# ログアウトAPI
@router.get("/logout")
def logout():
    pass