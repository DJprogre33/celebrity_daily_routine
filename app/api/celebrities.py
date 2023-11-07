from fastapi import APIRouter, Depends
from pydantic import UUID4

from app.abstractions.celebritiy_service import ICelebrityService
from app.abstractions.transaction_manager import ITransactionManager
from app.schemas.celebrity import CelebrityResponseSchema, DailyScheduleResponseSchema

celebrity_router = APIRouter(prefix="/celebrities", tags=["Celebrities"])


@celebrity_router.get("", response_model=CelebrityResponseSchema)
async def get_celebrities(
    celebrity_service: ICelebrityService = Depends(),
    transaction_manager: ITransactionManager = Depends(),
):
    existed_celebrities = await celebrity_service.get_celebrities(transaction_manager)
    return existed_celebrities


@celebrity_router.get(
    "/{celebrity_id}",
    response_model=DailyScheduleResponseSchema,
    responses={
        "404": {"description": "Celebrity not found"},
        "400": {"description": "Bad request"},
    },
)
async def get_shedule_by_celebrity_id(
    celebrity_id: UUID4,
    celebrity_service: ICelebrityService = Depends(),
    transaction_manager: ITransactionManager = Depends(),
):
    existed_celebrities = await celebrity_service.get_schedule_by_celebrity_id(
        celebrity_id, transaction_manager
    )
    return existed_celebrities
