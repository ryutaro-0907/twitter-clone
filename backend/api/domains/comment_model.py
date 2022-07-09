from datetime import datetime
from pydantic import BaseModel


class Comment(BaseModel):
    id: int
    created_at: datetime or str

    tweet_id: int
    user_id: int

    comment: str
    images: str or None = None

    blocked: bool = False

    updated_at: datetime or str = None
    deleted_at: datetime or str or None = None

    class Config:
        orm_mode = True


class InputComment(BaseModel):
    user_id: int
    tweet_id: int

    comment: str
    images: str or None = None

    class Config:
        orm_mode = True
