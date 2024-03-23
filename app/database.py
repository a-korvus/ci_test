"""Database settings."""

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

DB_URL: str = "sqlite+aiosqlite:///cookbook.db"

async_engine = create_async_engine(
    url=DB_URL,
    echo=True,
)

async_session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
)
