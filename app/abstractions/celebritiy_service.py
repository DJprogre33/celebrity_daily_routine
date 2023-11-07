import uuid
from abc import ABC, abstractmethod

from app.abstractions.transaction_manager import ITransactionManager
from app.schemas.celebrity import CelebrityResponseSchema, DailyScheduleResponseSchema


class ICelebrityService(ABC):
    @staticmethod
    @abstractmethod
    async def get_celebrities(
        transaction_manager: ITransactionManager,
    ) -> CelebrityResponseSchema:
        ...

    @staticmethod
    @abstractmethod
    async def get_schedule_by_celebrity_id(
        celebrity_id: uuid.UUID, transaction_manager: ITransactionManager
    ) -> DailyScheduleResponseSchema:
        ...
