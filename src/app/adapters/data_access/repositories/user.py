from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.users.entities import User
from app.domain.users.repositories import UserRepository
from app.adapters.data_access.models.user import UserDb


class SqlalchemyUserRepository(UserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_all_users(self, limit: int = 20, offset: int = 0) -> list[User]:
        query = select(UserDb).limit(limit).offset(offset)

        users_result = await self.session.execute(query)
        users = users_result.scalars()
        if users is None:
            return []

        return [user.to_entity() for user in users]

    async def get_user_by_id(self, user_id: int):
        stmt = select(UserDb).where(UserDb.id == user_id)

        user_result = await self.session.execute(stmt)
        user = user_result.scalar()
        if user is None:
            return None
        return user.to_entity()

    async def get_user_by_email(self, email: str):
        stmt = select(UserDb).where(UserDb.email == email)

        user_result = await self.session.execute(stmt)
        user = user_result.scalar()
        if user is None:
            return None
        return user.to_entity()

    async def create_user(self, name: str, email: str, hashed_password: str):
        stmt = insert(UserDb).values(
            name=name,
            email=email,
            hashed_password=hashed_password,
            is_active=False
        )
        await self.session.execute(stmt)
        

    async def update_user(self, name: str, email: str, hashed_password: str):
        stmt = update(UserDb).where(UserDb.email == email).values(
            name=name,
            hashed_password=hashed_password
        )
        await self.session.execute(stmt)
        
    async def delete_user(self, name: str, email: str, hashed_password: str):
        stmt = delete(UserDb).where(UserDb.email == email)
        await self.session.execute(stmt)