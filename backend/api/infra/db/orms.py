import profile
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from api.infra.db.base import Base


class TweetOrm(Base):
    __tablename__ = "tweets"
    id = Column(Integer, primary_key=True, nullable=False)
    text = Column(String(255))
    user_id = Column(Integer)
    images = Column(String(255))
    username = Column(String(255))
    profile_image = Column(String(255))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)

    comment = relationship("CommentOrm")


class CommentOrm(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, nullable=False)

    comment = Column(String(255))
    user_id = Column(Integer)
    tweet_id = Column(Integer, ForeignKey("tweets.id"))
    username = Column(String(255))

    images = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)


class UserOrm(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
