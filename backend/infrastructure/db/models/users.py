from typing import List

from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.infrastructure.db.base import Base


class User(Base):
    __tablename__ = "users"

    tid: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    role: Mapped[int] = mapped_column(ForeignKey("roles.id", ondelete="CASCADE"))
    first_name: Mapped[str]
    last_name: Mapped[str]
    phone_number: Mapped[int] = mapped_column(unique=True)

    application_forms: Mapped[List["ApplicationForm"]] = relationship(
        "ApplicationForm",
        back_populates="user",
        lazy="joined"
    )
    user_role: Mapped["Role"] = relationship("Role", back_populates="users", lazy="joined")
