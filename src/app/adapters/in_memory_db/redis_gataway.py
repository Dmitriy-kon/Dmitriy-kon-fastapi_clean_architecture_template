import os
import secrets

import redis.asyncio as aioredis

from app.application.abstraction.session_gateway import SessionGateway


class RedisConfData:
    def __init__(self) -> None:
        self.pool = aioredis.ConnectionPool(
            host=os.getenv("REDIS_HOST", "redisdb"),
            port=os.getenv("REDIS_PORT", "6379"),
            password=os.getenv("REDIS_PASSWORD", None),
            db=0,
        )
        self.expire = int(os.getenv("SESSION_EXPIRE", "3600"))


class RedisSessionGateway(SessionGateway):
    def __init__(self, config: RedisConfData) -> None:
        self.client = aioredis.Redis(connection_pool=config.pool)
        self.expire = config.expire

    async def create_session(self, user_name: str) -> str:
        session_id = secrets.token_hex(16)
        await self.client.set(session_id, user_name, self.expire)
        return session_id

    async def get_session(self, session_id: str) -> str | None:
        return await self.client.get(session_id)

    async def delete_session(self, session_id: str) -> None:
        await self.client.delete(session_id)
