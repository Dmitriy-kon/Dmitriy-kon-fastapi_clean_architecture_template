from app.application.abstraction.interactor import Interactor
from app.application.abstraction.login_processor import LoginProcessor
from app.application.dto.user import RequestUserUpdateDTO


class LoginUser(Interactor[RequestUserUpdateDTO, bool]):
    def __init__(self, login_processor: LoginProcessor) -> None:
        self.login_processor = login_processor

    async def __call__(self, user_dto: RequestUserUpdateDTO) -> bool:
        user_in_db = await self.login_processor.indentificate_user(user_dto)
        return self.login_processor.authenticate_user(user_dto, user_in_db)
