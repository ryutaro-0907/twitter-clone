from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    @staticmethod
    def get_password_hash(password: str) -> str:
        return pwd_cxt.hash(password)

    @staticmethod
    def verify_password(hashed_password: str, plain_password: str) -> bool:
        return pwd_cxt.verify(plain_password, hashed_password)
