class DomainError(Exception):
    """Base class for all domain exceptions."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
