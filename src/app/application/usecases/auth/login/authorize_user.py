from collections.abc import Callable
from app.application.dto.user import RequestUserDTO
from app.application.abstraction.interactor import Interactor
from app.application.common.exceptions import UserAlreadyExistsException, UserPasswordNotMatchException

from app.domain.users.repositories import UserRepository

from app.adapters.auth.password_process import hash_password, verify_password


class AuthorizeUser(Interactor[RequestUserDTO, str]):
    def __init__(self) -> str:
        self.check_password_processor = verify_password
        self.hash_password = hash_password
        

    def __call__(self, from_user_password: str, from_db_password: str) -> str:
        res = self.check_password_processor(from_user_password, from_db_password.encode())
        if not res:
            raise UserPasswordNotMatchException("Your password is not correct")
        return res
