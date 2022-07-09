import logging

from typing import List
from sqlalchemy.orm import Session

from dataclasses import dataclass

from api.domains.tweet_model import Tweet, InputTweet
from api.infra.db.orms import TweetOrm

logger = logging.getLogger(__name__)


@dataclass
class TweetDBHandler:
    session: Session

    def create_tweet(self, input: InputTweet) -> Tweet or None:
        try:
            tweet = TweetOrm(
                text=input.text, user_id=input.user_id, images=input.images
            )
            self.session.add(tweet)
            self.session.commit()
            logger.info("Tweet created successfully")
            return Tweet.from_orm(tweet)
        except Exception as e:
            logger.error("Error creating tweet: %s", e)

    def fetch_tweet_by_id(self, tweet_id: int) -> Tweet or None:
        try:
            tweet: Tweet = (
                self.session.query(Tweet).filter(Tweet.id == tweet_id).first()
            )
            return tweet
        except Exception as e:
            logger.error("could not fetch tweet: %s", e)
            return None

    def fetch_tweets(self) -> List[Tweet] or None:
        try:
            tweets = self.session.query(TweetOrm).all()
            return tweets
        except Exception as e:
            logger.error("could not fetch tweets: %s", e)
            return None

    def update_tweet(self, tweet_info: InputTweet) -> Tweet or None:
        try:
            tweet = (
                self.session.query(TweetOrm)
                .filter(TweetOrm.id == tweet_info.id)
                .first()
            )
            tweet.update({"text": tweet_info.text})
            self.session.commit()

            logger.info("updated tweet: %s", tweet)
            return Tweet.from_orm(tweet)

        except Exception as e:
            raise Exception("Could not update tweet: %s", e)

    def delete_tweet(self, tweet_id) -> None:
        try:
            self.session.query(TweetOrm).filter(TweetOrm.id == tweet_id).delete()
            logger.info("deleting tweet: %s", tweet_id)

        except Exception as e:
            raise Exception("Could not delete tweet: %s", e)
