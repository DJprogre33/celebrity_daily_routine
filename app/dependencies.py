from typing import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.abstractions.celebritiy_service import ICelebrityService
from app.abstractions.transaction_manager import ITransactionManager
from app.database import async_session_factory
from app.services.celebrity import CelebrityService
from app.transaction_manager import TransactionManager


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        try:
            yield session
        finally:
            await session.close()


def get_transaction_manager(
    session: AsyncSession = Depends(get_async_session),
) -> ITransactionManager:
    return TransactionManager(session)


def get_celebrity_service() -> ICelebrityService:
    return CelebrityService()
