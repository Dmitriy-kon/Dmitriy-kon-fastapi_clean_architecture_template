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
