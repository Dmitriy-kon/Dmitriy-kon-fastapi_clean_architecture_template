from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import HTTPException, Request

from app.application.abstraction.session_gateway import SessionGateway


@inject
async def sessionid_required(
    request: Request, session_gateway: FromDishka[SessionGateway]
) -> None:
    session_id = request.cookies.get("session_id")

    if (
        session_id is None
        or await session_gateway.get_session(session_id) is None
    ):
        raise HTTPException(status_code=401, detail="Invalid session id")
