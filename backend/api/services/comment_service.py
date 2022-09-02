from asyncio.log import logger
from sqlite3 import InternalError
from typing import List

from api.domains.comment_model import Comment, InputComment
from api.infra.db.comment_db import CommentDBHandler
from sqlalchemy.orm import Session


class CommentService:
    def __init__(self, session: Session):
        self.handler = CommentDBHandler(session)

    def create_comment(self, request: InputComment) -> Comment:
        logger.info("creating new comment")
        try:
            res = self.handler.create_comment(request)
            logger.info("created new comment")
            return res

        except Exception as e:
            raise InternalError("could not create comment: %s" % e)

    def update_comment(self, request: InputComment) -> Comment:
        res = self.handler.update_comment(request)
        return res

    def delete_comment(self, id: int) -> None:
        res = self.handler.delete_comment(id)
        return res

    def get_comments_by_id(self, tweet_id: int) -> Comment or List[Comment] or None:
        res = self.handler.fetch_comments_by_tweet_id(tweet_id)
        return res

    # def get_tweet(self, id: int) -> Tweet or None:
    #     res = self.handler.get_tweet(id)
    #     return res
