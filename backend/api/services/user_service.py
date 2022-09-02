from asyncio.log import logger
from typing import List
from api.domains.user_model import UserCreate, UserLogin, UserUpdate, UserDisplay
from api.infra.db.user_db import UserDBHandler
from sqlalchemy.orm import Session


class UserService:
    def __init__(self, session: Session):
        self.handler = UserDBHandler(session)

    def user_exist(self, email: str) -> bool:
        return self.handler.user_exist(email)

    def create_user(self, request: UserCreate) -> UserDisplay:
        logger.info("creating new user")
        res = self.handler.create_user(request)
        logger.info("created new user")
        return res

    def update_user(self, request: UserCreate) -> UserDisplay:
        res = self.handler.update_user(request)
        return res

    def delete_user(self, email: str) -> None:
        res = self.handler.delete_user(email)
        return res

    def user_login(self, request: UserLogin) -> UserDisplay:
        res = self.handler.user_login(request)
        return res
