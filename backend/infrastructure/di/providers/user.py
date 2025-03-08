from dishka import Provider, provide, Scope, AnyOf
from sqlalchemy.ext.asyncio import AsyncSession

from backend.infrastructure.db.repositories.user import UserRepository, IUserRepository


class UserRepositoryProvider(Provider):
    @provide(scope=Scope.REQUEST, provides=AnyOf[UserRepository, IUserRepository])
    async def get_repository(self, session: AsyncSession) -> IUserRepository:
        return UserRepository(session)
