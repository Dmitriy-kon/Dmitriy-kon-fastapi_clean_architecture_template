class EmailProcessor:
    def get_confirmation_code(self) -> str:
        raise NotImplementedError

    def send_message(self, message: str):
        raise NotImplementedError
