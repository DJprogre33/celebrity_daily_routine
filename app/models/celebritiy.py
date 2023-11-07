import uuid

from sqlalchemy.dialects.postgresql import JSONB, TEXT, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Celebrities(Base):
    __tablename__ = "celebrities"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID, default=uuid.uuid4, primary_key=True, index=True
    )
    name: Mapped[str]
    age: Mapped[int]
    occupation: Mapped[str]
    short_bio: Mapped[str] = mapped_column(TEXT)


class DailySchedule(Base):
    __tablename__ = "daily_schedule"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID, default=uuid.uuid4, primary_key=True, index=True
    )
    celebrity_id: Mapped[uuid.UUID] = mapped_column(UUID)
    schedule: Mapped[JSONB] = mapped_column(JSONB)
