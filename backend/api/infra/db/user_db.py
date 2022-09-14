from http.client import HTTPException
import logging

from sqlalchemy.orm import Session

from dataclasses import dataclass

from ...domains.user_model import UserDisplay, UserCreate, UserUpdate, UserLogin
from ...infra.db.orms import UserOrm
from ...infra.utils.pass_hassing import Hash

logger = logging.getLogger(__name__)


@dataclass
class UserDBHandler:
    session: Session

    def user_exists(self, email: str) -> bool:
        user_exist = self.session.query(UserOrm).filter(UserOrm.email == email).first()
        if user_exist is None:
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
            logger.info(f"User created successfully id:{user.id} email:{user.email}, date:{user.created_at}")

            # user_display = UserDisplay(
            #     id=user.id,
            #     username=user.username,
            #     email=user.email,
            # )
            user_display = UserDisplay.from_orm(user)

            return user_display

        except Exception as e:
            HTTPException(500, "Error creating user: {}".format(e))

    def user_login(self, input: UserLogin) -> UserDisplay:
        try:
            user = (
                self.session.query(UserOrm)
                .filter(UserOrm.email == input.email)
                .first()
            )
            user_disply = UserDisplay.from_orm(user)

            logger.info(f'user found: {user_disply}')

            if user_disply.id is None:
                raise HTTPException(500, "Internal Error: could not find uesr")

            logger.info('user found:', user_disply)

            if Hash.verify_password(user_disply.password, input.password):
                return UserDisplay.from_orm(user)

            else:
                raise ValueError("Invalid password")

        except Exception as e:
            raise HTTPException(500, "could not find user, please sign up: {}".format(e))

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
