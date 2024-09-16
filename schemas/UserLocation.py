from typing import Optional

from pydantic import BaseModel


class getUserLocations(BaseModel):
    id: int
    user_name: Optional[str]
    user_name_kana: Optional[str]
    area_id: int
    area_name: Optional[str]
    attendance_id: int
    attendance_status: Optional[str]

    class Config:
        orm_mode = True
