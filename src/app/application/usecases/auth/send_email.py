from app.application.abstraction.email_processor import EmailProcessor
from app.application.abstraction.interactor import Interactor
from app.application.abstraction.uow import UoW
from app.application.dto.user import RequestUserDTO
from app.domain.users.repositories import UserRepository


class SendEmailForUser(Interactor[RequestUserDTO, str]):
    def __init__(
        self,
        user_repository: UserRepository,
        uow: UoW,
        email_processor: EmailProcessor,
    ) -> None:
        self.user_repository = user_repository
        self.uow = uow
        self.email_processor = email_processor

    async def __call__(self, input_dto: RequestUserDTO) -> str:
        code = self.email_processor.get_confirmation_code()
        # save code in db
        self.email_processor.send_message()

        return code
