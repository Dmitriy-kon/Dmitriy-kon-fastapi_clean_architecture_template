from app.application.dto.user import (
    RequestUserDTO,
    ResponseUserDTO,
    RequestLimmitOffsetDTO,
)
from app.application.abstraction.interactor import Interactor
from app.application.common.exceptions import UserNotFoundException
from app.domain.users.entities import User
from app.domain.users.repositories import UserRepository


class GetAllUsers(Interactor[RequestLimmitOffsetDTO, list[ResponseUserDTO]]):
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def __call__(self, request: RequestLimmitOffsetDTO) -> list[ResponseUserDTO]:
        users: list[User] = await self.user_repository.get_all_users(
            request.limit, request.offset
        )
        if users is None or len(users) == 0:
            raise UserNotFoundException("Users not found")

        return [ResponseUserDTO.from_entity(user) for user in users]
