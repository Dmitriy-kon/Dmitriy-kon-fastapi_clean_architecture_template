from dataclasses import dataclass

from app.domain.common.value_objects import ValueObject


@dataclass
class UserId(ValueObject[int]):
    def validate(self):
        pass
