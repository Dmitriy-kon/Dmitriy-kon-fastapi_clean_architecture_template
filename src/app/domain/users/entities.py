from dataclasses import dataclass

from app.domain.common.entities import Entity
from app.domain.users.value_object import UserId


@dataclass
class User(Entity[UserId]):
    name: str
    email: str
    password: str
    is_active: bool

    @staticmethod
    def create(uid: int, name: str, email: str, password: str, *, is_active: bool):
        return User(
            id=UserId(uid),
            name=name,
            email=email,
            password=password,
            is_active=is_active,
        )
