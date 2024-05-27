from pydantic import BaseModel


class SUserOut(BaseModel):
    name: str
    email: str


class SUserIn(SUserOut):
    password: str
