from dishka import Provider, provide, Scope
from sqlalchemy.ext.asyncio import AsyncSession

from backend.infrastructure.db.repositories.user import UserRepository


class UserRepositoryProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_repository(self, session: AsyncSession) -> UserRepository:
        return UserRepository(session)
