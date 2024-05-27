from app.application.dto.user import RequestUserDTO, ResponseUserDTO
from app.application.abstraction.interactor import Interactor
from app.application.common.exceptions import UserNotFoundException

from app.domain.users.entities import User
from app.domain.users.repositories import UserRepository


class IdentificateUser(Interactor[RequestUserDTO, str]):
    def __init__(self, 
                 user_repository: UserRepository) -> str:
        self.user_repository = user_repository
    async def __call__(self, input_dto: RequestUserDTO) -> User:
        user = await self.user_repository.get_user_by_name(input_dto.name)
        if user is None:
            raise UserNotFoundException(f"User with name {input_dto.name} not found")
        
        return user
        
        