from abc import abstractmethod
from typing import Protocol

from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from backend.api.schemas import CreateForm
from backend.infrastructure.db import User


class IUserRepository(Protocol):

    @abstractmethod
    async def insert_user(
        self,
        tid: int,
        first_name: str,
        last_name: str,
        phone_number: str | None,
        email: str | None,
    ) -> None: ...

    @abstractmethod
    async def get_user_by_id(self, tid: int) -> User | None: ...

    @abstractmethod
    async def get_user_by_phone_number(self, phone_number: str) -> User | None: ...

    @abstractmethod
    async def update_user_phone_number(self, tid: int, phone_number: str) -> None: ...

    @abstractmethod
    async def update_user_email(self, info: CreateForm) -> None: ...


class UserRepository(IUserRepository):
    model: type[User] = User

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_user_by_id(self, tid: int) -> User | None:
        stmt = select(self.model).where(self.model.tid == tid)

        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def insert_user(
        self,
        tid: int,
        first_name: str,
        last_name: str | None,
        phone_number: str | None = None,
        email: str | None = None,
    ) -> None:
        stmt = insert(self.model).values(
            tid=tid,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
        )

        await self._session.execute(stmt)
        await self._session.commit()

    async def update_user_email(self, info: CreateForm) -> None:
        stmt = (
            update(self.model)
            .where(self.model.phone_number == info.phone_number)
            .values(email=info.email)
        )

        await self._session.execute(stmt)
        await self._session.commit()

    async def get_user_by_phone_number(self, phone_number: str) -> User | None:
        stmt = select(self.model).where(self.model.phone_number == phone_number)

        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def update_user_phone_number(self, tid: int, phone_number: str) -> None:
        stmt = (
            update(self.model)
            .where(self.model.tid == tid)
            .values(phone_number=phone_number)
        )

        await self._session.execute(stmt)
        await self._session.commit()
