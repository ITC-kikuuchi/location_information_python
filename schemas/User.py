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
