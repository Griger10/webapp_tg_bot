from abc import ABC, abstractmethod

from sqlalchemy import select, update, func
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from backend.api.schemas import CreateForm
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
            phone_number: str | None,
            email: str | None,
    ) -> None:
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
            last_name: str | None,
            phone_number: str | None = None,
            email: str | None = None
    ) -> None:
        stmt = insert(self.model).values(
            tid=tid,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email
        )

        stmt.on_conflict_do_nothing()

        await self._session.execute(stmt)
        await self._session.commit()

    async def update_user_phone_number_and_email(self, info: CreateForm) -> None:
        stmt = (
            update(self.model)
            .where(
                func.lower(self.model.first_name) == info.first_name.lower(),
                func.lower(self.model.last_name) == info.last_name.lower()
            )
            .values(
                phone_number=info.phone_number,
                email=info.email
            )
        )

        await self._session.execute(stmt)
        await self._session.commit()
