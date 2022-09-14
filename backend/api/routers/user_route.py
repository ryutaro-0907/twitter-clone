from cmath import isfinite
from genericpath import exists
from fastapi import APIRouter, Depends, HTTPException

from typing import List
from sqlalchemy.orm import Session

from ..domains.user_model import UserCreate, UserLogin, UserUpdate, UserDisplay
from ..infra.db.database import get_session
from ..services.user_service import UserService

import logging


logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/users", response_model=UserDisplay)
def create_user(request: UserCreate, session: Session = Depends(get_session)):

    try:
        service = UserService(session)

        # exists = service.user_exists(request.email)
        # if exists:
        #     raise HTTPException(409, "Conflict: this email is already taken, please login")

        try:
            res = service.create_user(request)
            if isinstance(res, UserDisplay):
                logger.info("User created successfully")
                return res
            else:
                HTTPException(404, "Couldn't create user")
        except Exception as e:
            HTTPException(500, "Couldn't create user", e)

    except Exception as e:
        raise HTTPException(500, "Intrnal server error:{}".format(e))


@router.post("/users/login", response_model=UserDisplay)
def user_login(request: UserLogin, session: Session = Depends(get_session)):
    try:
        service = UserService(session)
        res = service.user_login(request)
        if isinstance(res, UserDisplay):
            logger.info("login tweets")
            return res
        else:
            HTTPException(404, "Couldn't login", res)

    except Exception as e:
        return HTTPException(500, "Couldn't login", e)


@router.put("/user/{_id}/update", response_model=UserDisplay)
def update_user(request: UserUpdate, session: Session = Depends(get_session)):
    try:
        service = UserService(session)
        res = service.update_user(request)
        if isinstance(res, UserDisplay):
            logger.info("update user")
            return res
        else:
            HTTPException(404, "Couldn't update user")
    except Exception as e:
        HTTPException(500, "Couldn't update tweet", e)


@router.delete("/tweets/{_id}", response_model=UserDisplay)
def delete_user(email: str, session: Session = Depends(get_session)):
    try:
        service = UserService(session)
        service.delete_user(email)

        return "user deleted successfully"

    except Exception as e:
        HTTPException(500, "Couldn't create tweet", e)
