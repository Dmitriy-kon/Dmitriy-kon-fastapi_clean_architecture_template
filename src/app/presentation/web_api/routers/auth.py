from typing import Annotated

from fastapi import APIRouter

from app.adapters.auth.password_process import hash_password, verify_password
from app.presentation.web_api.schemas.user import SUser
from app.application.dto.user import RequestUserDTO, ResponseUserDTO

from app.application.usecases.auth.register_inactive_user import RegisterInactiveUser
from app.application.usecases.auth.check_user_unique import CheckUserUnique
from app.application.usecases.auth.send_email import EmailProcessor


auth_router = APIRouter()


@auth_router.post("/register")
async def register(user: SUser, 
                   register_inactive_user_interactor: RegisterInactiveUser,
                   check_user_unique_interactor: CheckUserUnique,
                   send_email_interactor: EmailProcessor):
    user.password = hash_password(user.password)

    user_dto = RequestUserDTO(name=user.name, email=user.email, password=user.password)
    await check_user_unique_interactor(user_dto)
    await register_inactive_user_interactor(user_dto)
    await send_email_interactor(user_dto)
    
