from datetime import datetime
from pydantic import BaseModel


class Comment(BaseModel):
    id: int

    tweet_id: int
    user_id: int
    username: str

    comment: str

    created_at: datetime
    updated_at: datetime 
    deleted_at: datetime = None

    blocked: bool = False

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
