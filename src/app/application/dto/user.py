from dataclasses import dataclass

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