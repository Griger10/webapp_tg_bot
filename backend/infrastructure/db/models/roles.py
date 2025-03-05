from typing import List

from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.infrastructure.db.base import Base


class Role(Base):
    __tablename__ = 'roles'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)

    users: Mapped[List["User"]] = relationship("User", back_populates="user_role")  # type: ignore

    def __repr__(self) -> str:
        return f"Role(id={self.id}, name={self.name})"
