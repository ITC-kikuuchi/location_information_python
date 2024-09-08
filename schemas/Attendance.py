from typing import Optional

from pydantic import BaseModel


class getAttendances(BaseModel):
    id: int
    attendance_status: Optional[str]

    class Config:
        orm_mode = True
