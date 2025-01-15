from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from backend.api.schemas import CreateForm


class IFormRepository(ABC):
    def __init__(self, session: AsyncSession):
        self._session = session

    @abstractmethod
    async def add_form(self, form: CreateForm):
        raise NotImplementedError


class FormRepository(IFormRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def add_form(self, form: CreateForm):
        pass
