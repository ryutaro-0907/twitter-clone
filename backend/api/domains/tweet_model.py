import json
from datetime import datetime

from pydantic import BaseModel


class Tweet(BaseModel):
    id: int

    user_id: int
    username: str

    text: str

    profile_image: str = None

    created_at: datetime
    updated_at: datetime
    deleted_at: datetime = None

    blocked: bool = False

    class Config:
        orm_mode = True


class InputTweet(BaseModel):
    user_id: int
    username: str

    text: str
    profile_image: str = None

    class Config:
        orm_mode = True

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value
