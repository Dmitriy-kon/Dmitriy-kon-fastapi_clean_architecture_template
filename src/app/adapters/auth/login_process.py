from app.adapters.auth.password_process import verify_password
from app.application.common.exceptions import (
    UserNotFoundError,
    UserPasswordNotMatchError,
)
from app.application.dto.user import RequestUserUpdateDTO
from app.domain.users.entities import User
from app.domain.users.repositories import UserRepository


class LoginProcessorSql:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def indentificate_user(self, user_dto: RequestUserUpdateDTO) -> User:
        user = await self.user_repository.get_user_by_name(user_dto.name)
        if user is None:
            raise UserNotFoundError(f"User with name {user_dto.name} not found")
        return user

    def authenticate_user(
        self, user_dto: RequestUserUpdateDTO, user_in_db: User
    ) -> bool:
        res = verify_password(user_dto.password, user_in_db.password)
        if not res:
            raise UserPasswordNotMatchError("Your password is not correct")
        return res
