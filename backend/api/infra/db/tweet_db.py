import logging
from dataclasses import dataclass
from http.client import HTTPException
from typing import List

from fastapi import UploadFile
from sqlalchemy.orm import Session

from ...domains.tweet_model import InputTweet, Tweet
from ...infra.db.orms import TweetImageOrm, TweetOrm

logger = logging.getLogger(__name__)


@dataclass
class TweetDBHandler:
    session: Session

    def create_tweet(self, input: InputTweet, files:list[UploadFile]=None) -> Tweet:
        try:
            logger.info(f'creating TweetOrm with: {input}')

            tweet = TweetOrm(
                text=input.text,
                user_id=input.user_id,
                username=input.username,
                profile_image=input.profile_image,
            )
            logger.info('TweetOrm created')

            # if files is not None:
            #     try:
            #         for file in files:
            #             file_handler = S3FileHandler()
            #             s3_dir = '/users/' + str(input.user_id) + '/' + str(tweet.id) + '/'
            #             s3_file = S3File(
            #                 file=file,
            #                 key=s3_dir + file.filename
            #             )
            #             object_path = file_handler.upload_file_to_s3(s3_file, s3_dir)

            #             tweet_image = TweetImageOrm(
            #                 tweet_id = tweet.id,
            #                 file_name = file.filename,
            #                 object_path = object_path,
            #             )

                #         self.session.add(tweet_image)
                #         # FIXME
                #         # Research if it's better to commit at once in the end.
                #         self.session.commit()
                # except Exception as e:
                #     raise Exception(f'Error while uploading files to s3 : {e}')

            self.session.add(tweet)
            self.session.commit()
            logger.info("Tweet created successfully")

            return Tweet.from_orm(tweet)

        except Exception as e:
            logger.error("Error creating tweet: %s", e)

    def fetch_tweet_by_id(self, tweet_id: int) -> Tweet:
        try:
            tweet: Tweet = (
                self.session.query(Tweet).filter(Tweet.id == tweet_id).first()
            )

            return tweet
        except Exception as e:
            logger.error("could not fetch tweet: %s", e)
            return None

    def fetch_tweets(self) -> List[Tweet]:
        try:
            tweets: List[Tweet] = self.session.query(TweetOrm).all()
            tweets.reverse()
            return tweets

        except Exception as e:
            raise HTTPException(500, "could not fetch tweets: %s", e)

    def update_tweet(self, info: InputTweet) -> Tweet:
        try:
            tweet: TweetOrm = (
                self.session.query(TweetOrm).filter(TweetOrm.id == info.id).first()
            )

            tweet.text = info.text
            tweet.images = info.images

            self.session.commit()

            logger.info("updated tweet: %s", tweet)
            return Tweet.from_orm(tweet)

        except Exception as e:
            raise Exception("Could not update tweet: %s", e)

    def delete_tweet(self, tweet_id: int) -> None:
        try:
            tweet = self.session.query(TweetOrm).filter(TweetOrm.id == tweet_id).first()
            res = Tweet.from_orm(tweet)

            try:
                self.session.delete(tweet)
                logger.info("deleting tweet: %s", tweet_id)
                return res

            except Exception as e:
                raise Exception("Could not delete tweet: %s", e)

        except Exception as e:
            raise Exception("Could not find tweet: %s", e)
