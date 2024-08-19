from typing import Optional

from pydantic import BaseModel


class getUsers(BaseModel):
    id: int
    user_name: Optional[str]
    user_name_kana: Optional[str]
    mail_address: Optional[str]
    is_admin: bool

    class Config:
        orm_mode = True

class createUser(BaseModel):
    user_name: Optional[str]
    user_name_kana: Optional[str]
    mail_address: Optional[str]
    password: Optional[str]
    is_admin: bool
    default_area_id: int
    
    class Config:
        orm_mode = True