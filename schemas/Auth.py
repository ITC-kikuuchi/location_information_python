from typing import Optional

from pydantic import BaseModel


class loginUser(BaseModel):
    id: int
    user_name: Optional[str]
    is_admin: bool

    class Config:
        orm_mode = True
