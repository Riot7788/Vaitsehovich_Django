from fastapi import APIRouter, FastAPI
from src.booking_app.routers.booking_router import router as booking_router

router = APIRouter(
    prefix="/books",
    tags=["Booking"]
)

router.include_router(booking_router)