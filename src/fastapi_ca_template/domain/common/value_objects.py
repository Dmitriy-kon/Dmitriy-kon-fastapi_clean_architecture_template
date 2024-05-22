from dataclasses import dataclass
from typing import Generic, TypeVar

ValueT = TypeVar("ValueT")


@dataclass
class ValueObject(Generic[ValueT]):
    __value: ValueT
    
    def get_value(self) -> ValueT:
        return self.__value
    
    def __post_init__(self):
        self.validate()
    
    def validate(self):
        """
        Implement validation logic here in your subclass.
        Raises ValueError if validation fails.
        """
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.get_value()!r})"
    