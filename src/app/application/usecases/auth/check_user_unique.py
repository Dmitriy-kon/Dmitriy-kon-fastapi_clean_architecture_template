from app.application.dto.user import RequestUserDTO
from app.application.abstraction.interactor import Interactor
from app.application.common.exceptions import UserAlreadyExistsException

from app.domain.users.repositories import UserRepository



class RegisterInactiveUser(Interactor[RequestUserDTO, str]):
    def __init__(self, 
                 user_repository: UserRepository) -> str:
        self.user_repository = user_repository

    async def __call__(self, 
                       input_dto: RequestUserDTO) -> str:

        user_by_email = await self.user_repository.get_user_by_email(input_dto.email)
        user_by_name = await self.user_repository.get_user_by_name(input_dto.name)
        
        if user_by_email is not None or user_by_name is not None:
            raise UserAlreadyExistsException
        
        
        return "ok"