from typing import AsyncIterable

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.config.db_config import get_db_config


class SessionProvider(Provider):
    scope = Scope.REQUEST

    config = get_db_config()

    engine = create_async_engine(config.dsn)

    session_maker = async_sessionmaker(engine, expire_on_commit=False)

    @provide
    async def get_session(self) -> AsyncIterable[AsyncSession]:
        async with self.session_maker() as session:
            yield session
