from dataclasses import dataclass

from app.domain.common.value_objects import ValueObject
from app.domain.exceptions.validate import DomainValidationException

@dataclass
class UserId(ValueObject[int]):
    def validate(self):
        pass
    