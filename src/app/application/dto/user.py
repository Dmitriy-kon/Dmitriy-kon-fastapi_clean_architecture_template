from dataclasses import dataclass

from app.domain.users.entities import User


@dataclass
class RequestUserDTO:
    name: str
    password: str
    email: str


@dataclass
class RequestUserUpdateDTO:
    name: str
    password: str


@dataclass
class RequestLimmitOffsetDTO:
    offset: int
    limit: int


@dataclass
class ResponseUserDTO:
    id: int
    name: str
    email: str
    is_active: bool

    @staticmethod
    def from_entity(entity: User) -> "ResponseUserDTO":
        return ResponseUserDTO(
            id=entity.id.get_value(),
            name=entity.name,
            email=entity.email,
            is_active=entity.is_active,
        )
