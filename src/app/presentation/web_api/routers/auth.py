from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Request, Response

from app.adapters.auth.password_process import hash_password
from app.application.abstraction.session_gateway import SessionGateway
from app.application.dto.user import RequestUserDTO, RequestUserUpdateDTO
from app.application.usecases.auth.check_user_unique import CheckUserUnique
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
    check_user_unique_interactor: FromDishka[CheckUserUnique],
):
    user.password = hash_password(user.password)
    user_dto = RequestUserDTO(name=user.name, email=user.email, password=user.password)

    await check_user_unique_interactor(user_dto)
    return await register_inactive_user_interactor(user_dto)


@auth_router.post("/login")
async def login_json(
    user: SUserLogin,
    login_user_interactor: FromDishka[LoginUser],
    session_gateway: FromDishka[SessionGateway],
    req: Request,
    res: Response,
):
    result = await login_user_interactor(
        RequestUserUpdateDTO(name=user.name, password=user.password)
    )

    old_session_id = req.cookies.get("session_id")
    old_session_res = None

    if old_session_id:
        old_session_res = await session_gateway.get_session(old_session_id)
    if old_session_res:
        await session_gateway.delete_session(old_session_id)

    session_id = await session_gateway.create_session(user.name)

    res.set_cookie(key="session_id", value=session_id, max_age=3600, httponly=True)

    return {"message": result}
