from sqlalchemy.ext.asyncio import AsyncSession

from app.abstractions.transaction_manager import ITransactionManager
from app.repositories.celebrity import CelebrityRepository


class TransactionManager(ITransactionManager):
    def __init__(self, db: AsyncSession):
        self._db = db
        self.celebrities = CelebrityRepository(self._db)

    async def __aenter__(self) -> None:
        pass

    async def __aexit__(self, *args) -> None:
        await self._db.rollback()

    async def commit(self) -> None:
        await self._db.commit()

    async def rollback(self):
        await self._db.rollback()
