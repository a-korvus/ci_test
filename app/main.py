"""The main entry point to the FastAPI app."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from .queries import create_tables, delete_tables, insert_data
from .router import router

description = """
## Нere you can get information about all recipes \
and detailed information about each of them
"""


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Delete old tables and create new tables."""
    print("Application is running")
    await delete_tables()
    print("Database cleared")
    await create_tables()
    print("Database created")
    await insert_data()
    print("Tables created")
    yield
    print("Application has been terminated")


# app = FastAPI(lifespan=lifespan)
app = FastAPI(
    title="Cookbook API",
    description=description,
    summary="Small cookbook API",
    version="0.0.1",
    docs_url="/cookbook/api/docs",
    redoc_url=None,
)
app.include_router(router=router)
