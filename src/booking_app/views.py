from django.shortcuts import render
from django.http import HttpResponse


users = [
    {
        "user_id": 1,
        "name": "Ann",
        "age": 25,
        "comment": "Cool"
    },
    {
        "user_id": 2,
        "name": "Bob",
        "age": 27,
        "comment": "Nice"
    },
    {
        "user_id": 3,
        "name": "John",
        "age": 30,
        "comment": "Super"
    },
    {
        "user_id": 4,
        "name": "Max",
        "age": 31,
        "comment": "Great"
    }
]

hotels = [
    {
        "hotel_id": 1,
        "name": "Minsk",
        "address": "Avenue Nezavisimosti, 21",
        "star": 4
    },
    {
        "hotel_id": 2,
        "name": "Prezident Hotel",
        "address": "Kirova, 18",
        "star": 5
    },
    {
        "hotel_id": 3,
        "name": "Renaissance",
        "address": " Dzerzhinsky Avenue, 1E",
        "star": 4
    },
    {
        "hotel_id": 4,
        "name": "DoubleTree by Hilton Minsk",
        "address": "Avenue Pobeditelei, 9",
        "star": 4
    }
]

def some_template_view (request):
    return render(
        request=request,
        template_name="base.html",
    )

def home_view(request):
    return render(
        request=request,
        template_name="home.html"
    )

def user_view(request):
    context = {
        "users": users
    }
    return render(
        request=request,
        template_name="user.html",
        context=context
    )

def comment_user(request):
    context = {
        "users": users
    }
    return render(
        request=request,
        template_name="comment_user.html",
        context=context
    )

def all_apartments(request):
    context = {
        "hotels": hotels
    }
    return render(
        request=request,
        template_name="all_hotel.html",
        context=context
    )