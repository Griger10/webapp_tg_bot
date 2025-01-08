from typing import List

from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.db.base import Base


class User(Base):
    __tablename__ = "users"

    tid: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    phone_number: Mapped[int]

    application_forms: Mapped[List["ApplicationForm"]] = relationship(
        "ApplicationForm",
        back_populates="user"
    )
