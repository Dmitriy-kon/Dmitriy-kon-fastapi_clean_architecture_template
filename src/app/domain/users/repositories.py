from typing import Protocol


from app.domain.users.entities import User

class UserRepository(Protocol):
    async def get_all_users(self,
                            limit: int = 20,
                            offset: int = 0) -> list[User]:
        raise NotImplementedError
    
    async def get_user_by_id(self, user_id: int):
        raise NotImplementedError
    
    async def get_user_by_email(self, email: str):
        raise NotImplementedError
    
    async def create_user(self, name: str, email: str, hashed_password: str):
        raise NotImplementedError
    
    async def update_user(self, name: str, email: str, hashed_password: str):
        raise NotImplementedError
    
    async def delete_user(self, name: str, email: str, hashed_password: str):
        raise NotImplementedError
        