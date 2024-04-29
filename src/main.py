from fastapi import FastAPI
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import re

from src.auth.routers.base import router as auth_router
from src.booking_app.routers.base import router as book_router

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth_router)
app.include_router(book_router)


@app.get("/base")
def base_html(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

def valid_input(text: str) -> bool:
    return not bool(re.match(r'^[a-zA-Zа-яА-Я\s]+$', text))

@app.get("/all_users")
def users_html(request: Request):
    users = [
        {"id": 1,
         "first_name": "Александр",
         "last_name": "Пупкин",
         "age": 46,
         "email": "some_email",
         "sex": "male"
         },
        {"id": 2,
         "first_name": "Максим",
         "last_name": "Дудкин",
         "age": 35,
         "email": "some_email",
         "sex": "male"
         },
        {"id": 3,
         "first_name": "Владимир",
         "last_name": "Великий",
         "age": 30,
         "email": "some_email",
         "sex": "male"
         },
        {"id": 4,
         "first_name": "Алексей",
         "last_name": "Воробей",
         "age": 55,
         "email": "some_email",
         "sex": "male"
         },
        {"id": 5,
         "first_name": "Михаил",
         "last_name": "Адамович",
         "age": 24,
         "email": "some_email",
         "sex": "male"
         },
        {"id": 6,
         "first_name": "Анна",
         "last_name": "Мунтян",
         "age": 20,
         "email": "some_email",
         "sex": "female"
         },
        {"id": 7,
         "first_name": "Натали",
         "last_name": "Мороз",
         "age": 21,
         "email": "some_email",
         "sex": "female"
         },
        {"id": 8,
         "first_name": "Марина",
         "last_name": "Воранцова",
         "age": 22,
         "email": "some_email",
         "sex": "female"
         },
        {"id": 9,
         "first_name": "Александра",
         "last_name": "Гурник",
         "age": 23,
         "email": "some_email",
         "sex": "female"
         },
        {"id": 10,
         "first_name": "Екатерина",
         "last_name": "Ефремова",
         "age": 24,
         "email": "some_email",
         "sex": "female"
         },
        {"id": 11,
         "first_name": "$$$Макс$$$",
         "last_name": "Корж",
         "age": 14,
         "email": "some_email",
         "sex": "male"
         }]

    return templates.TemplateResponse(request=request,
                                      name="users.html",
                                      context={"data": 2222, "users": users, "valid_input": valid_input})



