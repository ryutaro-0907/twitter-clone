from fastapi import APIRouter, Depends, HTTPException

from typing import List
from sqlalchemy.orm import Session

from api.domains.comment_model import Comment, InputComment
from api.infra.db.database import get_session
from api.services.comment_service import CommentService

import logging


logger = logging.getLogger(__name__)
router = APIRouter()


@router.post('/comments', response_model=Comment)
def create_comment(request: InputComment, session: Session = Depends(get_session)):
    service = CommentService(session)
    try:
        res = service.create_comment(request)
        if type(res) == Comment:
            logger.info("Comment created successfully")
            return res
        else:
            HTTPException(404, "Couldn't create comment")

    except Exception as e:
        HTTPException(500, "Couldn't create comment", e)


@router.get('/comments', response_model=List[Comment] or Comment)
def get_comments(tweet_id:int, session: Session = Depends(get_session)):
    try:
        service = CommentService(session)
        res = service.get_comments_by_id(tweet_id=tweet_id)
        if res is not None:
            logger.info('get comments')
            return res
        else:
            HTTPException(404, "Couldn't get comments", res)
    except Exception as e:
        return HTTPException(500, "Couldn't get comments", e)

@router.put("/comments/{_id}/update", response_model=Comment)
def update_tweet(request: InputComment, session: Session = Depends(get_session)):
    try:
        service = CommentService(session)
        res = service.update_comment(request)
        if res is not None:
            logger.info('update tweet')
            return res
        else:
            HTTPException(404, "Couldn't update tweet")
    except Exception as e:
        HTTPException(500, "Couldn't update tweet", e)

@router.delete('/comments/{_id}', response_model=Comment)
def delete_tweet(request: InputComment, session: Session = Depends(get_session)):
    try:
        service = CommentService(session)
        res = service.delete_comment(request)
        if res is not None:
            logger.info('delete tweet')
            return res
        else:
            HTTPException(404, "Couldn't create tweet")
    except Exception as e:
        HTTPException(500, "Couldn't create tweet", e)
