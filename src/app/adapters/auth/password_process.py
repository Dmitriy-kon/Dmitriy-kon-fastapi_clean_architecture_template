import bcrypt

from app.application.abstraction.password_process import PasswordManager


class PasswordManagerBcrypt(PasswordManager):
    def hash_password(self, password: str) -> str:
        salt: bytes = bcrypt.gensalt()
        hashed_password: bytes = bcrypt.hashpw(password.encode(), salt)
        return hashed_password.decode()

    def verify_password(self, password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode(), hashed_password.encode())
