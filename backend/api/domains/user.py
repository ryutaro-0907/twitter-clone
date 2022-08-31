from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int
    created_at: str

    username: str
    email: str
    password: str

    hassed_password: str

    updated_at: str = None
    deleted_at: str = None

    class Config:
        orm_mode = True


class InputComment(BaseModel):
    username: str
    email: str
    password: str

    profile_image: str = None

    class Config:
        orm_mode = True
