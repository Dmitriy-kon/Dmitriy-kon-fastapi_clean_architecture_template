from app.application.abstraction.interactor import Interactor
from app.application.abstraction.password_process import PasswordManager
from app.application.abstraction.uow import UoW
from app.application.common.exceptions import UserAlreadyExistsError
from app.application.dto.user import RequestUserDTO
from app.domain.users.repositories import UserRepository


class RegisterInactiveUser(Interactor[RequestUserDTO, str]):
    def __init__(
        self,
        user_repository: UserRepository,
        password_manager: PasswordManager,
        uow: UoW,
    ) -> None:
        self.user_repository = user_repository
        self.password_manager = password_manager
        self.uow = uow

    async def __call__(self, input_dto: RequestUserDTO) -> str:
        user_by_email = await self.user_repository.get_user_by_email(input_dto.email)
        if user_by_email is not None:
            raise UserAlreadyExistsError("Email already exists")

        user_by_name = await self.user_repository.get_user_by_name(input_dto.name)
        if user_by_name is not None:
            raise UserAlreadyExistsError("Name already exists")

        await self.user_repository.create_user(
            name=input_dto.name,
            email=input_dto.email,
            hashed_password=self.password_manager.hash_password(input_dto.password),
        )

        await self.uow.commit()

        return "ok"
