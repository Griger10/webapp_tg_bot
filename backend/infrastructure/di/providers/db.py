from collections.abc import AsyncIterable

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncEngine

from backend.config.models import DatabaseConfig


class SessionProvider(Provider):
    scope = Scope.APP

    @provide
    async def get_engine(self, db_config: DatabaseConfig) -> AsyncIterable[AsyncEngine]:
        engine = create_async_engine(db_config.dsn)
        yield engine
        await engine.dispose(True)

    @provide
    async def get_session_maker(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(engine, expire_on_commit=False)

    @provide(scope=Scope.REQUEST)
    async def get_session(self, pool: async_sessionmaker[AsyncSession]) -> AsyncIterable[AsyncSession]:
        async with pool() as session:
            yield session
