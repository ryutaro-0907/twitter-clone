import logging
from typing import List

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session

from ..domains.tweet_model import InputTweet, Tweet
from ..infra.db.database import get_session
from ..services.tweet_service import TweetService

logger = logging.getLogger(__name__)
router = APIRouter()


# @router.post("/tweets", response_model=Tweet)
# async def create_tweet(request: InputTweet, files: List[UploadFile] = File(...) or None,
#  session: Session = Depends(get_session)):
@router.post("/tweets/create", response_model=Tweet)
async def create_tweet(request: InputTweet = Form(...),
                       files: List[UploadFile] = File(None),
                       session: Session = Depends(get_session),
                       ) -> Tweet:

    try:
        service = TweetService(session)

        try:
            logger.info(
                f'request recived {request} with attachments {files}'
            )
            res = service.create_tweet(request=request, files=files)
            if isinstance(res, Tweet):
                logger.info("Tweet created successfully")
                return res
            else:
                HTTPException(404, "Couldn't create tweet")
        except Exception as e:
            HTTPException(500, "Couldn't create tweet", e)
    except Exception as e:
        logger.error("could not create service instance")


@router.get("/tweets", response_model=List[Tweet])
def get_tweets(session: Session = Depends(get_session)):
    try:
        service = TweetService(session)
        res = service.get_tweets()
        if res is not None:
            logger.info("get tweets")
            return res
        else:
            HTTPException(404, "Couldn't get tweets", res)
    except Exception as e:
        return HTTPException(500, "Couldn't get tweets", e)


@router.put("/tweets/{_id}/update", response_model=Tweet)
def update_tweet(request: InputTweet, session: Session = Depends(get_session)):
    try:
        service = TweetService(session)
        res = service.update_tweet(request)
        if res is not None:
            logger.info("update tweet")
            return res
        else:
            HTTPException(404, "Couldn't update tweet")
    except Exception as e:
        HTTPException(500, "Couldn't update tweet", e)


@router.delete("/tweets/{_id}", response_model=Tweet)
def delete_tweet(tweet_id: int, session: Session = Depends(get_session)):
    try:
        service = TweetService(session)
        res = service.delete_tweet(tweet_id)
        if res is not None:
            logger.info("delete tweet")
            return res
        else:
            HTTPException(404, "Couldn't create tweet")
    except Exception as e:
        HTTPException(500, "Couldn't create tweet", e)
