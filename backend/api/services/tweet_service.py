from asyncio.log import logger
from typing import List

from ..domains.tweet_model import Tweet, InputTweet
from ..infra.db.tweet_db import TweetDBHandler


from fastapi import UploadFile
from sqlalchemy.orm import Session


class TweetService:
    def __init__(self, session: Session):
        self.session = session
        self.handler = TweetDBHandler(self.session)

    def create_tweet(self, request: InputTweet, files: List[UploadFile]=None) -> Tweet or None:
        logger.info("creating new Tweet")
        res = self.handler.create_tweet(request, files)
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
