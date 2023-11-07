from fastapi import APIRouter

from app.api.celebrities import celebrity_router

main_router: APIRouter = APIRouter(prefix="/api")

main_router.include_router(celebrity_router)
