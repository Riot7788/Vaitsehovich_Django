from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserForm, HotelCommentForm
from .models import (
    Person, Hotel, HotelsComment, Hobby,
)


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


def all_users(request):
    context = {
        "persons": Person.objects.all().prefetch_related("hobbies")
    }
    return render(
        request=request,
        template_name="all_user.html",
        context=context
    )


def create_user_new(request):
    if request.method == 'POST':

        form = UserForm(request.POST)
        # import pdb;pdb.set_trace()
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse("all_user"))
    else:
        form = UserForm()
    context = {
        "form": form
    }
    return render(
        request=request,
        template_name="create_user.html",
        context=context
    )


def feedback_view(request):
    if request.method == 'POST':
        form = HotelCommentForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('hotel')
    else:
        form = HotelCommentForm()
    context = {
        "form": form
    }
    return render(
        request=request,
        template_name="feedback_form.html",
        context=context
    )