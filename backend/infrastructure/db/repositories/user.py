from abc import ABC, abstractmethod

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.infrastructure.db import User


class IUserRepository(ABC):
    model = User

    def __init__(self, session: AsyncSession):
        self._session = session

    @abstractmethod
    async def insert_user(
            self,
            tid: int,
            first_name: str,
            last_name: str,
            phone_number: int,
    ) -> int:
        raise NotImplementedError

    @abstractmethod
    async def get_user_by_id(self, tid: int) -> User:
        raise NotImplementedError


class UserRepository(IUserRepository):
    model = User

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_user_by_id(self, tid: int) -> User | None:
        stmt = select(self.model).where(self.model.tid == tid)

        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def insert_user(
            self,
            tid: int,
            first_name: str,
            last_name: str,
            phone_number: int,
    ) -> int:
        user = User(
            tid=tid,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number
        )

        self._session.add(user)
        await self._session.commit()
        return user.tid

