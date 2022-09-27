from datetime import datetime

from sqlalchemy import (TIMESTAMP, Boolean, Column, DateTime, ForeignKey,
                        Integer, String)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ...infra.db.base import Base


class TweetOrm(Base):
    __tablename__ = "tweets"
    id = Column(Integer, primary_key=True, nullable=True)
    text = Column(String(255))
    user_id = Column(Integer)
    # images = Column(String(255))
    username = Column(String(255))
    profile_image = Column(String(255))
    created_at = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now)
    updated_at = Column(
        TIMESTAMP(timezone=False),
        nullable=False,
        default=datetime.now,
        onupdate=datetime.now
    )
    deleted = Column(Boolean, nullable=False, default=False)

    comment = relationship("CommentOrm")

    images = relationship("TweetImageOrm", backref="tweets")


class TweetImageOrm(Base):
    __tablename__ = "tweet_images"

    id = Column(Integer, primary_key=True, index=True)
    tweet_id = Column(Integer, ForeignKey("tweets.id"), nullable=False)
    file_name = Column(String, nullable=False)
    object_path = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())


class CommentOrm(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)

    comment = Column(String(255))
    user_id = Column(Integer)
    tweet_id = Column(Integer, ForeignKey("tweets.id"))
    username = Column(String(255))

    images = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now)
    updated_at = Column(
        TIMESTAMP(timezone=False),
        nullable=False,
        default=datetime.now,
        onupdate=datetime.now
    )
    deleted = Column(Boolean, nullable=False, default=False)


class UserOrm(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

    created_at = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now)
    updated_at = Column(
        TIMESTAMP(timezone=False),
        nullable=False,
        default=datetime.now,
        onupdate=datetime.now
    )
    deleted = Column(Boolean, nullable=False, default=False)
