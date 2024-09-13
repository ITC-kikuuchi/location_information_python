from typing import Optional

from pydantic import BaseModel


class getUserStatus(BaseModel):
    id: int
    user_status: Optional[str]

    class Config:
        orm_mode = True
