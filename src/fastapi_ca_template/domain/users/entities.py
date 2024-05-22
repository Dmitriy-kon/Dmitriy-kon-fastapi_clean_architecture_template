from dataclasses import dataclass

from fastapi_ca_template.domain.common.entities import Entity
from fastapi_ca_template.domain.exceptions.validate import DomainValidationException
from fastapi_ca_template.domain.users.value_object import UserId


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
    
    
