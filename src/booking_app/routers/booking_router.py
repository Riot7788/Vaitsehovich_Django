from fastapi import APIRouter
import random

from src.settings import DB_PORT, DB_HOST

router = APIRouter(
    prefix="",
    tags=["Booking"]
)

@router.get("/items")
def random_five_num_list():
    numbers = []
    for i in range(5):
        numbers.append(random.randint(1, 100))
    return numbers

@router.get("/")
def get_query_params() -> dict:
    return {
        "DB_PORT": "some port",
        "DB_HOST": "some host",
    }
