from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.auth.enums import UserRole
from src.core.models import Base
from src.booking_app.models import Booking
from src.core.models.base import (
    str_30,
    created_at,
    updated_at,
)


class User(Base):
    first_name: Mapped[str_30] = mapped_column(nullable=False)
    last_name: Mapped[str_30] = mapped_column(nullable=False)
    role: Mapped[UserRole] = mapped_column(nullable=True)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    booking: Mapped[list["Booking"]] = relationship("Booking", back_populates="user")