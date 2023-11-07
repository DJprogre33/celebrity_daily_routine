import uuid

from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import MultipleResultsFound

from app.abstractions.celebritiy_service import ICelebrityService
from app.abstractions.transaction_manager import ITransactionManager
from app.schemas.celebrity import CelebrityResponseSchema, DailyScheduleResponseSchema


class CelebrityService(ICelebrityService):
    @staticmethod
    async def get_celebrities(
        transaction_manager: ITransactionManager,
    ) -> CelebrityResponseSchema:
        domain_celebrities = await transaction_manager.celebrities.get_celebrities()
        existed_celebrities = CelebrityResponseSchema(celebrities=domain_celebrities)
        return existed_celebrities

    @staticmethod
    async def get_schedule_by_celebrity_id(
        celebrity_id: uuid.UUID, transaction_manager: ITransactionManager
    ) -> DailyScheduleResponseSchema:
        try:
            domain_schedule = (
                await transaction_manager.celebrities.get_schedule_by_celebrity_id(
                    celebrity_id
                )
            )
        except MultipleResultsFound as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST) from e

        if not domain_schedule:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        existed_schedule = DailyScheduleResponseSchema.model_validate(domain_schedule)
        return existed_schedule
