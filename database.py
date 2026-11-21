import ssl

from sqlalchemy import make_url
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)
from sqlalchemy.orm import DeclarativeBase

from core.config import settings


DATABASE_URL = make_url(settings.DATABASE_URL)

# Use asyncpg driver
if DATABASE_URL.drivername in ("postgres", "postgresql"):
    DATABASE_URL = DATABASE_URL.set(
        drivername="postgresql+asyncpg"
    )

# Neon requires SSL
query_params = dict(DATABASE_URL.query)
query_params.pop("sslmode", None)

DATABASE_URL = DATABASE_URL.set(query=query_params)

ssl_context = ssl.create_default_context()

engine = create_async_engine(
    DATABASE_URL,
    connect_args={"ssl": ssl_context},
    pool_pre_ping=True
)


AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)


class Base(DeclarativeBase):
    pass


async def get_db():
    async with AsyncSessionLocal() as db:
        yield db
