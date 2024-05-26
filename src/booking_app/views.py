
from django.http import HttpResponse
from .models import Person, Hotel
from django.shortcuts import render
from django.views import View

users = [
    {
        "user_id": 1,
        "name": "Ann",
        "age": 25,
        "comment": "Cool"
    },
]

hotels = [
    {
        "hotel_id": 1,
        "name": "Minsk",
        "address": "Avenue Nezavisimosti, 21",
        "star": 4
    },
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
        "persons": Person.objects.all().prefetch_related("hotel_comments").prefetch_related("hobbies")
    }
    return render(
        request=request,
        template_name="persons.html",
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
        "hotels": Hotel.objects.all().prefetch_related("hotel_comments")
    }
    return render(
        request=request,
        template_name="all_hotel.html",
        context=context
    )
