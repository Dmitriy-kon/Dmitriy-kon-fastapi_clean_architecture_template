from typing import Annotated

from fastapi import APIRouter, Depends

from app.application.dto.user import RequestUserDTO, ResponseUserDTO

from app.presentation.web_api.schemas.user import SUser

user_router = APIRouter()


@user_router.get("/")
async def get_all_users() -> list[ResponseUserDTO]:
    pass

async def get_user_by_email(user_email: str) -> ResponseUserDTO:
    pass


