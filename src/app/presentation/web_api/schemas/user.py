from pydantic import BaseModel


class SUser(BaseModel):
    name: str
    email: str
    password: str