from datetime import datetime
from pydantic import BaseModel


class Tweet(BaseModel):
    id: int

    created_at: str
    user_id: int
    username: str
    profile_image: str

    text: str
    images: str = None

    updated_at: str = None
    deleted_at: str = None
    blocked: bool = False

    class Config:
        orm_mode = True


class InputTweet(BaseModel):
    user_id: int
    username: str
    profile_image: str

    text: str
    created_at: str

    images: str = None

    class Config:
        orm_mode = True
