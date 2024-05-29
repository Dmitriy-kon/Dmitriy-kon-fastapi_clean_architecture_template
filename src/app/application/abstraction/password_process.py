from typing import Protocol


class PasswordManager(Protocol):
    def hash_password(self, password: str) -> str:
        raise NotImplementedError

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        raise NotImplementedError
