from typing import Optional

from pydantic import BaseModel


class getAreas(BaseModel):
    id: int
    area_name: Optional[str]
    is_default_area: bool

    class Config:
        orm_mode = True