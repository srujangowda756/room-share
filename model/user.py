import uuid
from datetime import datetime, timezone

from sqlalchemy import Column,String,DateTime,Boolean,Enum
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from model.enum import Gender, Diet, Mode, OccupationCategory


class User(Base):
    __tablename__ = "users"

    id=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    phone = Column(String(15), unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)

    gender = Column(Enum(Gender, name="gender_enum"), nullable=True)
    diet = Column(Enum(Diet, name="diet_enum"), nullable=True)
    occupation_category = Column(
        Enum(OccupationCategory, name="occupation_category_enum"), nullable=True
    )
    occupation_text = Column(String, nullable=True)
    hometown_city = Column(String, nullable=True)

    mode = Column(
        Enum(Mode, name="mode_enum"), nullable=False, default=Mode.looking
    )
    phone_verified = Column(Boolean, nullable=False, default=False)
    is_blocked = Column(Boolean, nullable=False, default=False)

    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(tz=timezone.utc),
    )
