from typing import Protocol


class UserRepository(Protocol):
    async def get_all_users(self,
                            limit: int = 20,
                            offsert: int = 0) -> list:
        raise NotImplementedError
    
    async def get_user_by_id(self, user_id: int):
        raise NotImplementedError
    
    async def get_user_by_email(self, email: str):
        raise NotImplementedError
    
    async def create_user(self, user):
        raise NotImplementedError
    
    async def update_user(self, user):
        raise NotImplementedError
    
    async def delete_user(self, user):
        raise NotImplementedError
        