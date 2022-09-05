from datetime import datetime
from pydantic import BaseModel


class Tweet(BaseModel):
    id: int

    user_id: int
    username: str

    text: str

    images: str = None
    profile_image: str = None

    created_at: str = None
    updated_at: str = None
    deleted_at: str = None

    blocked: bool = False

    class Config:
        orm_mode = True


class InputTweet(BaseModel):
    user_id: int
    username: str

    text: str
    images: str = None
    profile_image: str = None

    class Config:
        orm_mode = True
