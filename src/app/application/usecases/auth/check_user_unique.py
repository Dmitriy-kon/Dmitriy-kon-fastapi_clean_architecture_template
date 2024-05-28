from app.application.abstraction.interactor import Interactor
from app.application.common.exceptions import UserAlreadyExistsError
from app.application.dto.user import RequestUserDTO
from app.domain.users.repositories import UserRepository


class CheckUserUnique(Interactor[RequestUserDTO, str]):
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def __call__(self, input_dto: RequestUserDTO) -> str:
        user_by_email = await self.user_repository.get_user_by_email(
            input_dto.email
        )
        if user_by_email is not None:
            raise UserAlreadyExistsError("Email already exists")

        user_by_name = await self.user_repository.get_user_by_name(
            input_dto.name
        )
        if user_by_name is not None:
            raise UserAlreadyExistsError("Name already exists")

        return "ok"
