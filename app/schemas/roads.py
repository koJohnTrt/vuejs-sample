from pydantic import BaseModel
from datetime import datetime

# データ取得用定義
class RoadsSelect(BaseModel):
    rec_id: int
    code: str
    name: str 
    date_from: datetime
    date_to: datetime

    class Config:
        orm_mode = True