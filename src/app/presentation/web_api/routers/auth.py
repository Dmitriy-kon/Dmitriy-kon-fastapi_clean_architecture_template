from typing import Annotated


from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Depends, Request, Response

from app.adapters.auth.password_process import hash_password, verify_password
from app.application.abstraction.session_gateway import SessionGateway
from app.presentation.web_api.schemas.user import SUserIn, SUserLogin
from app.application.dto.user import RequestUserDTO, ResponseUserDTO

from app.application.usecases.auth.register_inactive_user import RegisterInactiveUser
from app.application.usecases.auth.check_user_unique import CheckUserUnique
from app.application.usecases.auth.login.identificate_user import IdentificateUser
from app.application.usecases.auth.login.authorize_user import AuthorizeUser
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

@auth_router.post("/login")
async def login_json(user: SUserLogin,
                     identificate_user_interactor: FromDishka[IdentificateUser],
                     authorize_user_interactor: FromDishka[AuthorizeUser],
                     session_gateway: FromDishka[SessionGateway],
                     req: Request,
                     res: Response,
                     ):
    user_dto = RequestUserDTO(name=user.name, password=user.password)
    user_in_db = await identificate_user_interactor(user_dto)

    result = authorize_user_interactor(user_dto.password, user_in_db.password)
    
    session_id = req.cookies.get("session_id")
    session_res = None
    
    if session_id:
        session_res = await session_gateway.get_session(session_id)
    if session_res:
        await session_gateway.delete_session(session_id)
    session_id = await session_gateway.create_session(user_in_db.name)

    res.set_cookie("session_id", session_id, max_age=3600, httponly=True)
    
    return {}
