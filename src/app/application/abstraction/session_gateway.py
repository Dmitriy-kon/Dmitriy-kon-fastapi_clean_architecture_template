from typing import Protocol


class SessionGateway(Protocol):
    async def create_session(self, user_id: int) -> str:
        raise NotImplementedError
    
    async def get_session(self, session_id: str) -> str:
        raise NotImplementedError
    
    async def delete_session(self, session_id: str) -> None:
        raise NotImplementedError