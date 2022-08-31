from datetime import datetime
from pydantic import BaseModel


class Comment(BaseModel):
    id: int
    created_at: datetime or str

    tweet_id: int
    user_id: int
    username: str

    comment: str
    images: str = None

    blocked: bool = False

    updated_at: str = None
    deleted_at: str = None

    class Config:
        orm_mode = True


class InputComment(BaseModel):
    user_id: int
    tweet_id: int
    username: str

    comment: str
    images: str = None

    class Config:
        orm_mode = True
