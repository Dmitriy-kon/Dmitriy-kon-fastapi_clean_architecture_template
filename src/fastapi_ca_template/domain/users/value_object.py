from dataclasses import dataclass

from fastapi_ca_template.domain.common.value_objects import ValueObject
from fastapi_ca_template.domain.exceptions.validate import DomainValidationException

@dataclass
class UserId(ValueObject[int]):
    def validate(self):
        pass