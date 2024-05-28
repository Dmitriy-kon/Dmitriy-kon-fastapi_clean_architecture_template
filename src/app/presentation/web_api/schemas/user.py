from pydantic import BaseModel, EmailStr


class SUserOut(BaseModel):
    name: str
    email: EmailStr


class SUserIn(SUserOut):
    password: str


class SUserLogin(BaseModel):
    name: str
    password: str
