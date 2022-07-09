from asyncio.log import logger
from typing import List
from api.domains.tweet_model import Tweet, InputTweet
from api.infra.db.tweet_db import TweetDBHandler
from pydantic import BaseModel
from sqlalchemy.orm import Session


class TweetService:
    def __init__(self, session: Session):
        self.session = session
        self.handler = TweetDBHandler(self.session)

    def create_tweet(self, request: InputTweet) -> Tweet or None:
        logger.info("creating new Tweet")
        res = self.handler.create_tweet(request)
        logger.info("created new Tweet")
        return res

    def update_tweet(self, request: InputTweet) -> Tweet or None:
        res = self.handler.update_tweet(request)
        return res

    def delete_tweet(self, tweet_id: int) -> None:
        res = self.handler.delete_tweet(tweet_id)
        return res

    def get_tweets(self) -> List[Tweet] or None:
        res = self.handler.fetch_tweets()
        return res

    def get_tweet(self, id: int) -> Tweet or None:
        res = self.handler.get_tweet(id)
        return res
