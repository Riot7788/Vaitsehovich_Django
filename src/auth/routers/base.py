from fastapi import APIRouter, FastAPI
from src.auth.routers.user_router import router as user_router

router = APIRouter(
    prefix="/authentication",
    tags=["Authentication"]
)

router.include_router(user_router)