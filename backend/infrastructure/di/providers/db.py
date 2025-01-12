from typing import AsyncIterable

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from backend.config.db_config import get_db_config
from backend.infrastructure.db.repositories import HolderRepository


class SessionProvider(Provider):
    scope = Scope.REQUEST

    config = get_db_config()

    engine = create_async_engine(config.dsn)

    session_maker = async_sessionmaker(engine, expire_on_commit=False)

    @provide
    async def get_session(self) -> AsyncIterable[AsyncSession]:
        async with self.session_maker() as session:
            yield session


class HolderRepositoryProvider(Provider):

    scope = Scope.REQUEST

    @provide
    async def get_repository(self, session: AsyncSession) -> HolderRepository:
        return HolderRepository(session)
