"""Init Dev DB."""
import logging
import os


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.domains.tweet_model import InputTweet
from api.infra.db.base import Base
from api.infra.db.tweet_db import TweetDBHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if os.environ.get('db', 'sqlite'):
    SQLALCHEMY_DATABASE_URL = "sqlite:///./twitter_app.db"

else:
    db_user = os.environ.get('DB_USER', 'user')
    db_pass = os.environ.get('DB_PASS', 'pass')
    db_endpoint = os.environ.get('DB_ENDPOINT', 'localhost:5432')

    SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_pass}@{db_endpoint}/app_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def init() -> None:
    """init."""
    with SessionLocal() as db:
        handler = TweetDBHandler(db)
        tweet = InputTweet(user_id=1, text='test tweet')
        handler.create_tweet(tweet)


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
