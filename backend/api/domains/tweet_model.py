from datetime import datetime
from pydantic import BaseModel

class Tweet(BaseModel):
    id: int
    created_at: datetime or str
    text: str
    user_id: int
    images: str or None = None
    updated_at: datetime or str = None
    deleted_at: datetime or str or None =None
    blocked: bool or None = None

    class Config:
        orm_mode = True

class InputTweet(BaseModel):
    user_id: int
    text: str
    images: str or None = None

    class Config:
        orm_mode=True
