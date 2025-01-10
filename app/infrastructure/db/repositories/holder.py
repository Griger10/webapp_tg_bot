from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.repositories.user import UserRepository


class HolderRepository:
    def __init__(self, session: AsyncSession):
        self.user = UserRepository(session)
        self.form = ApplicationFormRepository(session)