from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str

    created_at: str
    updated_at: str
    deleted_at: str = None


class UserLogin(BaseModel):
    email: str
    password: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    username: str = None
    email: str = None
    password: str = None


class UserDisplay(UserBase):
    id: int
    class Config():
        orm_mode = True


if __name__ == '__main__':
    user = UserCreate(
        username="test",
        email="test@example.com",
        created_at="0000/00/00",
        updated_at="0000/00/00",
        password="test",
    )
    print(user)