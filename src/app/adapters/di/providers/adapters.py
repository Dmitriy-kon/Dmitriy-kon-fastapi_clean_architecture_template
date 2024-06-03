from collections.abc import AsyncIterable

from dishka import Provider, Scope, alias, from_context, provide
from fastapi import Request, Response
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.adapters.auth.password_process import PasswordManagerBcrypt
from app.adapters.auth.session_auth import SessionAuthAdapter
from app.adapters.data_access.repositories.user import SqlalchemyUserRepository
from app.adapters.in_memory_db.redis_gataway import (
    RedisConfData,
    RedisSessionGateway,
)
from app.application.abstraction.password_process import PasswordManager
from app.application.abstraction.session_gateway import SessionGateway
from app.application.abstraction.uow import UoW
from app.domain.users.repositories import UserRepository
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

    @provide(scope=Scope.REQUEST, provides=AsyncSession)
    async def provide_session(
        self, sessionmaker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        async with sessionmaker() as session:
            yield session

    # @provide(scope=Scope.REQUEST, provides=UoW)
    # async def provide_uow(
    #     self, session_maker: async_sessionmaker[AsyncSession]
    # ) -> AsyncIterable[AsyncSession]:
    #     async with session_maker() as session:
    #         yield session

    # @provide(scope=Scope.REQUEST, provides=UoW)
    # async def provide_uow(
    #     self, session: AsyncSession
    # ) -> AsyncSession:
    #     return session

    user_repository = provide(
        SqlalchemyUserRepository, scope=Scope.REQUEST, provides=UserRepository
    )

    password_manager = provide(
        PasswordManagerBcrypt, scope=Scope.REQUEST, provides=PasswordManager
    )

    uow = alias(source=AsyncSession, provides=UoW)


class InDbProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_redis_conf(self) -> RedisConfData:
        return RedisConfData()

    redis_sessions = provide(
        RedisSessionGateway, scope=Scope.REQUEST, provides=SessionGateway
    )


class SessionAuthProvider(Provider):
    scope = Scope.REQUEST

    request = from_context(provides=Request, scope=Scope.REQUEST)
    # response = from_context(provides=Response, scope=Scope.REQUEST)

    @provide(scope=Scope.REQUEST)
    def provide_auth(
        self, request: Request, session_gateway: SessionGateway
    ) -> SessionAuthAdapter:
        return SessionAuthAdapter(request, session_gateway)
