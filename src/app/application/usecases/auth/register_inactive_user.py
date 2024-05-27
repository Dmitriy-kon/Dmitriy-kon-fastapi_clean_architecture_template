from app.application.dto.user import RequestUserDTO
from app.application.abstraction.interactor import Interactor
from app.application.abstraction.uow import UoW

from app.domain.users.repositories import UserRepository



class RegisterInactiveUser(Interactor[RequestUserDTO, str]):
    def __init__(self, 
                 user_repository: UserRepository,
                 uow: UoW,) -> str:
        self.user_repository = user_repository
        self.uow = uow

    async def __call__(self, 
                       input_dto: RequestUserDTO) -> str:
        
        await self.user_repository.create_user(
            name=input_dto.name,
            email=input_dto.email,
            hashed_password=input_dto.password
        )
        # print("from uow", self.uow.get_transaction())
        await self.uow.commit()
        
        return "ok"
# class RegisterInactiveUser(Interactor[RequestUserDTO, str]):
#     def __init__(self, 
#                  user_repository: UserRepository) -> str:
#         self.user_repository = user_repository


#     async def __call__(self, 
#                        input_dto: RequestUserDTO) -> str:
        
#         await self.user_repository.create_user(
#             name=input_dto.name,
#             email=input_dto.email,
#             hashed_password=input_dto.hashed_password
#         )
        
#         return "ok"