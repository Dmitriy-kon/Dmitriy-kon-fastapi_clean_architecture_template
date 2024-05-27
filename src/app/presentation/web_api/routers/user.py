from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Depends, Request

from app.application.dto.user import (
    RequestUserDTO,
    ResponseUserDTO,
    RequestLimmitOffsetDTO,
)
from app.presentation.web_api.schemas.user import SUserIn, SUserOut
from app.presentation.web_api.schemas.limit_offset import SLimitOffset
from app.application.usecases.user.users import GetAllUsers

from app.adapters.auth.sessions_process import sessionid_required

user_router = APIRouter(tags=["users"], prefix="/users", route_class=DishkaRoute)


# @user_router.get("/")
# async def get_all_users(
#     session: FromDishka[SessionProcess],
#     request: Request,
#     schema: Annotated[SLimitOffset, Depends()], 
#     interactor: FromDishka[GetAllUsers]
# ) -> list[SUserOut]:
#     session(request)
#     return await interactor(
#         RequestLimmitOffsetDTO(limit=schema.limit, offset=schema.offset)
#     )
@user_router.get("/", dependencies=[Depends(sessionid_required)])
async def get_all_users(
    schema: Annotated[SLimitOffset, Depends()], 
    interactor: FromDishka[GetAllUsers]
) -> list[SUserOut]:
    return await interactor(
        RequestLimmitOffsetDTO(limit=schema.limit, offset=schema.offset)
    )


async def get_user_by_email(user_email: str) -> ResponseUserDTO:
    pass
