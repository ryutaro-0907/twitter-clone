import logging

from typing import List
from sqlalchemy.orm import Session

from dataclasses import dataclass

from api.domains.user_model import UserDisplay, UserCreate, UserUpdate, UserLogin
from api.infra.db.orms import UserOrm
from api.infra.utils.pass_hassing import Hash

logger = logging.getLogger(__name__)


@dataclass
class UserDBHandler:
    session: Session

    def user_exists(self, email: str) -> bool:
        user_exist = self.session.query(UserOrm).filter(UserOrm.email == email)
        if user_exist:
            return True
        else:
            return False

    def create_user(self, input: UserCreate) -> UserDisplay:
        try:
            user = UserOrm(
                username=input.username,
                email=input.email,
                password=Hash.get_password_hash(input.password),
            )
            self.session.add(user)
            self.session.commit()
            logger.info("User created successfully")
            logger.info(user.created_at)

            user_display = UserDisplay(
                id=user.id,
                username=user.username,
                email=user.email,
            )
            user_display = UserDisplay.from_orm(user)

            return user_display

        except Exception as e:
            logger.error("Error creating user: %s", e)

    def user_login(self, input: UserLogin) -> UserDisplay:
        try:
            user: UserOrm = (
                self.session.query(UserOrm).filter(UserOrm.email == input.email).first()
            )

            if Hash.verify_password(user.password, input.password):
                return UserDisplay.from_orm(user)

            else:
                raise ValueError("Invalid password")

        except Exception as e:
            logger.error("could not find user, please sign up: %s", e)
            return None

    def update_user(self, input: UserUpdate) -> UserDisplay:
        try:
            user: UserOrm = (
                self.session.query(UserOrm).filter(UserOrm.email == input.email).first()
            )

            user.username = input.username
            user.email = input.email
            user.password = input.password

            self.session.commit()

            logger.info("updated user: %s", user)
            return UserDisplay.from_orm(user)

        except Exception as e:
            raise Exception("Could not update tweet: %s", e)

    def delete_user(self, email: str) -> None:
        try:
            user = self.session.query(UserOrm).filter(UserOrm.email == email).first()
            res = UserDisplay.from_orm(user)

            try:
                self.session.delete(user)
                logger.info("user deleted")
                return res

            except Exception as e:
                raise Exception("Could not delete user: %s", e)

        except Exception as e:
            raise Exception("Could not find user: %s", e)
