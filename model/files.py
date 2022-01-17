from pydantic import BaseModel
from typing import Optional

class MusicInfo(BaseModel):
    ID: int
    CATEGORY: str
    FILENAME: str
    