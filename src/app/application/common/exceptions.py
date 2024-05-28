class ApplicationError(Exception):
    """Base class for all application exceptions."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class UserAlreadyExistsError(ApplicationError):
    pass


class UserNotFoundError(ApplicationError):
    pass


class UserPasswordNotMatchError(ApplicationError):
    pass
