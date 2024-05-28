from typing import Protocol

from app.application.dto.user import RequestUserUpdateDTO
from app.domain.users.entities import User


class LoginProcessor(Protocol):
    async def indentificate_user(self, user_dto: RequestUserUpdateDTO) -> User:
        raise NotImplementedError

    def authenticate_user(
        self, user_dto: RequestUserUpdateDTO, user_in_db: User
    ) -> bool:
        raise NotImplementedError
