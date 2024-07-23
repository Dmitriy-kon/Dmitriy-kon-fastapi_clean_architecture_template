from fastapi import Request, Response

from app.application.abstraction.session_gateway import SessionGateway


class SessionAuthAdapter:
    def __init__(self, request: Request, session_gateway: SessionGateway) -> None:
        self.request = request
        self.session_gateway = session_gateway

    async def delete_session_if_exists(self) -> None:
        session_id: str | None = self.request.cookies.get("session_id")
        session_data = None

        if session_id:
            session_data = await self.session_gateway.get_session(session_id)
        if session_data:
            await self.session_gateway.delete_session(session_id)

    async def create_session(self, user_name: str) -> str:
        return await self.session_gateway.create_session(user_name)

    def set_session_cookie(self, response: Response, session_id: str) -> None:
        response.set_cookie(key="session_id", value=session_id, httponly=True)
