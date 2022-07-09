import logging

from typing import List
from sqlalchemy.orm import Session

from dataclasses import dataclass

from api.domains.comment_model import Comment, InputComment
from api.infra.db.orms import CommentOrm

logger = logging.getLogger(__name__)

@dataclass
class CommentDBHandler:
    session: Session

    def create_comment(self, input: InputComment) -> Comment:
        try:
            comment = CommentOrm(comment=input.comment, user_id=input.user_id, tweet_id=input.tweet_id, images=input.images)
            logger.info('creating comment')
            self.session.add(comment)
            self.session.commit()

            logger.info({
                'action': 'comment created',
                'data': Comment.from_orm(comment)
            })

            logger.info("Comment created successfully")
            return Comment.from_orm(comment)

        except Exception as e:
            logger.error("Error creating comment: %s", e)
            raise Exception("Error creating comment: %s" % e)

    def fetch_comments_by_tweet_id(self, tweet_id:int) -> Comment or List[Comment] or None:
        try:
            comments = self.session.query(CommentOrm).filter(CommentOrm.tweet_id == tweet_id).all()
            return comments
        except Exception as e:
            logger.error('could not fetch comments: %s', e)
            raise Exception('Could not fetch comments')

    # def fetch_Comments(self) -> List[Comment] or None:
    #     try:
    #         tweets = self.session.query(CommentOrm).all()
    #         return tweets
    #     except Exception as e:
    #         logger.error('could not fetch tweets: %s', e)
    #         return None

    def update_comment(self, info: InputComment) -> Comment or None:
        try:
            comment = self.session.query(CommentOrm).filter(CommentOrm.id == info.id).first()
            comment.update({'text': info.comment})
            self.session.commit()

            logger.info('updated tweet: %s', tweet)
            return Comment.from_orm(tweet)

        except Exception as e:
            raise Exception('Could not update tweet: %s', e)

    def delete_comment(self, comment_id: int) -> None:
        try:
            self.session.query(CommentOrm).filter(CommentOrm.id == comment_id).delete()
            logger.info('deleting tweet: %s', comment_id)

        except Exception as e:
            raise Exception('Could not delete tweet: %s', e)