from typing import List

from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.infrastructure.db import Base


class Role(Base):
    __tablename__ = 'roles'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)

    users: Mapped[List["User"]] = relationship("User", back_populates="user_role")