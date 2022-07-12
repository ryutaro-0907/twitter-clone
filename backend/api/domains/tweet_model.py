from datetime import datetime
from pydantic import BaseModel


class Tweet(BaseModel):
    id: int
    created_at: datetime or str

    text: str
    user_id: int
    username: str
    profile_image: str

    images: str or None = None
    updated_at: datetime or str = None
    deleted_at: datetime or str or None = None
    blocked: bool or None = False

    class Config:
        orm_mode = True


class InputTweet(BaseModel):
    user_id: int
    text: str
    username: str
    profile_image: str

    images: str or None = None
    class Config:
        orm_mode = True
