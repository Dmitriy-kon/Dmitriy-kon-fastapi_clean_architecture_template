from typing import Annotated


from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from app.adapters.auth.password_process import hash_password, verify_password
from app.presentation.web_api.schemas.user import SUserIn
from app.application.dto.user import RequestUserDTO, ResponseUserDTO

from app.application.usecases.auth.register_inactive_user import RegisterInactiveUser
from app.application.usecases.auth.check_user_unique import CheckUserUnique
from app.application.usecases.auth.send_email import EmailProcessor


auth_router = APIRouter(tags=["auth"], prefix="/auth", route_class=DishkaRoute)


@auth_router.post("/register")
async def register(user: SUserIn, 
                   register_inactive_user_interactor: FromDishka[RegisterInactiveUser],
                   check_user_unique_interactor: FromDishka[CheckUserUnique]):
    user.password = hash_password(user.password)

    user_dto = RequestUserDTO(name=user.name, email=user.email, password=user.password)
    await check_user_unique_interactor(user_dto)
    res = await register_inactive_user_interactor(user_dto)
    return res
    # await send_email_interactor(user_dto)
    
