from dataclasses import dataclass

from app.domain.users.entities import User

@dataclass
class RequestUserDTO:
    name: str
    email: str
    password: str

@dataclass
class ResponseUserDTO:
    id: int
    name: str
    email: str
    is_active: bool
    
    
    def from_entity(self, entity: User) -> "ResponseUserDTO":
        return ResponseUserDTO(
            id=entity.id.get_value(),
            name=entity.name,
            email=entity.email,
            is_active=entity.is_active
        )
        