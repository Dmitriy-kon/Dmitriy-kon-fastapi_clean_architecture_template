from typing import AsyncIterable

from dishka import Provider, Scope, provide, AnyOf
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)

from app.domain.users.repositories import UserRepository
from app.adapters.data_access.repositories.user import SqlalchemyUserRepository
from app.application.abstraction.uow import UoW
from app.main.config import DatabaseConfig


class SqlalchemyProvier(Provider):
    @provide(scope=Scope.APP)
    def provide_config(self) -> DatabaseConfig:
        return DatabaseConfig.from_env()

    @provide(scope=Scope.APP)
    def provide_engine(self, config: DatabaseConfig) -> AsyncEngine:
        return create_async_engine(config.db_uri, echo=True)

    @provide(scope=Scope.APP)
    def provide_sessionmaker(
        self, engine: AsyncEngine
    ) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(
            bind=engine, class_=AsyncSession, expire_on_commit=False
        )

    @provide(scope=Scope.REQUEST, provides=AnyOf[AsyncSession, UoW])
    async def provide_session(
        self, sessionmaker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        async with sessionmaker() as session:
            yield session

    # @provide(scope=Scope.SESSION, provides=UoW)
    # async def provide_uow(
    #     self, sessionmaker: async_sessionmaker[AsyncSession]
    # ) -> AsyncIterable[UoW]:
    #     async with sessionmaker() as uow:
    #         yield uow
    # @provide(scope=Scope.REQUEST, provides=UoW)
    # async def provide_uow(
    #     self, sessionmaker: async_sessionmaker[AsyncSession]
    # ) -> AsyncIterable[UoW]:
    #     async with sessionmaker() as uow:
    #         yield uow
    
    user_repository = provide(SqlalchemyUserRepository, scope=Scope.REQUEST, provides=UserRepository)

    # async_session = provide(AsyncSession, scope=Scope.REQUEST, provides=UoW)
