from app.application.abstraction.interactor import Interactor
from app.application.abstraction.password_process import PasswordManager
from app.application.common.exceptions import (
    UserNotFoundError,
    UserPasswordNotMatchError,
)
from app.application.dto.user import RequestUserUpdateDTO
from app.domain.users.repositories import UserRepository


class LoginUser(Interactor[RequestUserUpdateDTO, bool]):
    def __init__(
        self, user_repository: UserRepository, password_manager: PasswordManager
    ) -> None:
        self.user_repository = user_repository
        self.password_manager = password_manager

    async def __call__(self, user_dto: RequestUserUpdateDTO) -> bool:
        user_in_db = await self.user_repository.get_user_by_name(user_dto.name)
        if user_in_db is None:
            raise UserNotFoundError(f"User with name {user_dto.name} not found")

        result = self.password_manager.verify_password(
            user_dto.password, user_in_db.password
        )
        if not result:
            raise UserPasswordNotMatchError("Your password is not correct")

        return result
