"""Init Dev DB."""
import logging
import os
import profile


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import contextlib
from sqlalchemy import MetaData

from api.domains.tweet_model import InputTweet
from api.domains.comment_model import InputComment
from api.domains.user_model import UserCreate
from api.infra.db.base import Base
from api.infra.db.user_db import UserDBHandler
from api.infra.db.tweet_db import TweetDBHandler
from api.infra.db.comment_db import CommentDBHandler


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# if os.environ.get('db', 'sqlite'):
#     SQLALCHEMY_DATABASE_URL = "sqlite:///./twitter_app.db"

# else:
#     db_user = os.environ.get('DB_USER', 'user')
#     db_pass = os.environ.get('DB_PASS', 'pass')
#     db_endpoint = os.environ.get('DB_ENDPOINT', 'localhost:5432')

#     SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_pass}@{db_endpoint}/app_db"

db_user = os.environ.get("DB_USER", "user")
db_pass = os.environ.get("DB_PASS", "pass")
db_endpoint = os.environ.get("DB_ENDPOINT", "development-db:5432")

SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_pass}@{db_endpoint}/app_db"


engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def insert_initial_data_to_db() -> None:
    with SessionLocal() as db:
        handler = UserDBHandler(db)
        user = UserCreate(username='string', email='string', password='string', created_at='2000/09/01', updated_at='2000/09/01')
        handler.create_user(user)

        handler = TweetDBHandler(db)

        tweet = InputTweet(
            user_id=1,
            text="For now, you can only add text and comment. Also login function is not implemented yet.",
            username="Test user",
            profile_image="https://links.papareact.com/gll",
            created_at="2015-07-01T00:00:00",
        )
        handler.create_tweet(tweet)

        handler = CommentDBHandler(db)
        comment = InputComment(
            user_id=1, tweet_id=1, username="comment user", comment="test comment"
        )
        handler.create_comment(comment)


def clear_db() -> None:
    meta = MetaData()
    with contextlib.closing(engine.connect()) as con:
        trans = con.begin()
        for table in reversed(meta.sorted_tables):
            con.execute(table.delete())
        trans.commit()


def main() -> None:
    insert_initial_data_to_db()
    clear_db()


if __name__ == "__main__":
    main()
