from dataclasses import dataclass

from app.domain.common.entities import Entity
from app.domain.exceptions.validate import DomainValidationException
from app.domain.users.value_object import UserId


@dataclass
class User(Entity[UserId]):
    name: str
    email: str
    password: str
    is_active: bool

    def validate(self):
        pass
    
    @staticmethod
    def create(
        id: int,
        name: str,
        email: str,
        password: str,
        is_active: bool
    ):
        return User(
            id=UserId(id),
            name=name,
            email=email,
            password=password,
            is_active=is_active
        )
    
    
