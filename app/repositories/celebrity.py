import uuid
from typing import Optional, Sequence, Type

from sqlalchemy import RowMapping, delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import Base
from app.models.celebritiy import Celebrities, DailySchedule


class CelebrityRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_celebrities(self) -> Sequence[RowMapping]:
        query = select(Celebrities.__table__.columns)
        result = await self.session.execute(query)
        return result.mappings().all()

    async def get_schedule_by_celebrity_id(
        self, celebrity_id: uuid.UUID
    ) -> Optional[RowMapping]:
        query = select(DailySchedule.__table__.columns).where(
            DailySchedule.celebrity_id == celebrity_id
        )
        result = await self.session.execute(query)
        return result.mappings().one_or_none()

    async def insert_celebrity_data(self, **celebrity_data) -> None:
        await self.__insert_data(Celebrities, **celebrity_data)

    async def insert_daily_schedule_data(self, **daily_schedule_data) -> None:
        await self.__insert_data(DailySchedule, **daily_schedule_data)

    async def __insert_data(self, model: Type[Base], **data) -> None:
        query = insert(model).values(data)
        await self.session.execute(query)

    async def clear_database(self) -> None:
        clear_celebrities = delete(Celebrities)
        cleare_daily_schedule = delete(DailySchedule)
        await self.session.execute(clear_celebrities)
        await self.session.execute(cleare_daily_schedule)
