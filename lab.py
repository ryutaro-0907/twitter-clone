from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Boolean, Integer, String

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    is_active = Column(Boolean, default=True)




from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str

    crated_at: str
    updated_at: str
    deleted_at: str = None

class UserCreateOrUpdate(UserBase):
    password: str

class UserDisplay(UserBase):
    id: int
    class Config():
        orm_mode = True


from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import UserCreate
from db.models import User


def create_user(db: Session, request: UserCreate):
    new_user = User(
        username = request.username,
        email = request.email,
        password = Hash.get_password_hash(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


from schemas import UserCreate, UserDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user


router = APIRouter(
  prefix='/user',
  tags=['user']
)

@router.post('/', response_model=UserDisplay)
def create_user(request: UserCreate, db: Session = Depends(get_db)):
  return db_user.create_user(db, request)