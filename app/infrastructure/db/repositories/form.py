from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession


class IFormRepository(ABC):
    def __init__(self, session: AsyncSession):
        self._session = session

    @abstractmethod
    async def add_form(self, form: CreateForm):
        raise NotImplementedError
