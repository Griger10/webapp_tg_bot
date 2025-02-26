from typing import List

from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.infrastructure.db.base import Base


class User(Base):
    __tablename__ = "users"

    tid: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    role: Mapped[int] = mapped_column(ForeignKey("roles.id", ondelete="CASCADE"), default=0)
    first_name: Mapped[str]
    last_name: Mapped[str]
    phone_number: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]

    user_role: Mapped["Role"] = relationship("Role", back_populates="users")
