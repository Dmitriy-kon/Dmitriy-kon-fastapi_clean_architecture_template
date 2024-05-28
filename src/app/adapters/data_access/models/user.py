from typing import cast

from sqlalchemy.orm import Mapped, mapped_column

from app.adapters.data_access.models.base import Base, TimeMixin
from app.domain.users.entities import User


class UserDb(TimeMixin, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(server_default="false")

    def to_entity(self) -> User:
        return User.create(
            uid=cast(int, self.id),
            name=cast(str, self.name),
            email=cast(str, self.email),
            password=cast(str, self.hashed_password),
            is_active=cast(bool, self.is_active),
        )
