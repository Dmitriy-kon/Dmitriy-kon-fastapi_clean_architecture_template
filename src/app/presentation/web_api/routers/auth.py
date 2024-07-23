from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Response

from app.adapters.auth.session_auth import SessionAuthAdapter
from app.application.dto.user import RequestUserDTO, RequestUserUpdateDTO
from app.application.usecases.auth.login_user import LoginUser
from app.application.usecases.auth.register_inactive_user import (
    RegisterInactiveUser,
)
from app.presentation.web_api.schemas.user import SUserIn, SUserLogin

auth_router = APIRouter(tags=["auth"], prefix="/auth", route_class=DishkaRoute)


@auth_router.post("/register")
async def register(
    user: SUserIn,
    register_inactive_user_interactor: FromDishka[RegisterInactiveUser],
):
    user_dto = RequestUserDTO(name=user.name, email=user.email, password=user.password)

    return await register_inactive_user_interactor(user_dto)


@auth_router.post("/login")
async def login_json(
    user: SUserLogin,
    response: Response,
    login_user_interactor: FromDishka[LoginUser],
    session_auth_adapter: FromDishka[SessionAuthAdapter],
):
    result = await login_user_interactor(
        RequestUserUpdateDTO(name=user.name, password=user.password)
    )
    await session_auth_adapter.delete_session_if_exists()
    session_id = await session_auth_adapter.create_session(user.name)
    session_auth_adapter.set_session_cookie(response, session_id)

    return {"message": result}
