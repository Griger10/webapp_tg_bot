from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.infrastructure.db.base import Base


class ApplicationForm(Base):
    __tablename__ = 'application_forms'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    goal: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.tid', ondelete='CASCADE'))

    user: Mapped["User"] = relationship('User', back_populates="application_forms")
