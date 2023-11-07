import asyncio

from fastapi import FastAPI

from app.abstractions.celebritiy_service import ICelebrityService
from app.abstractions.transaction_manager import ITransactionManager
from app.database import async_session_factory
from app.dependencies import get_celebrity_service, get_transaction_manager
from app.logic.database_seeder import DatabaseSeeder
from app.routers import main_router
from app.transaction_manager import TransactionManager


def create_app() -> FastAPI:
    _app = FastAPI()
    init_main_router(_app)
    init_dependencies(_app)
    asyncio.create_task(fill_database())
    return _app


def init_main_router(_app: FastAPI) -> None:
    _app.include_router(main_router)


def init_dependencies(_app: FastAPI) -> None:
    _app.dependency_overrides[ITransactionManager] = get_transaction_manager
    _app.dependency_overrides[ICelebrityService] = get_celebrity_service


async def fill_database() -> None:
    db = async_session_factory()
    database_seeder = DatabaseSeeder(
        "app/celebrities_data.json", TransactionManager(db)
    )
    await database_seeder.fill_database()
    await db.close()
