from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserForm, HotelCommentForm
from .models import (Person, Hotel, HotelsComment, Hobby,)
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.decorators.cache import cache_page

comments = [
    {
        "number": 1,
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

@cache_page(60 * 30)
def some_template_view(request):
    return render(
        request=request,
        template_name="base.html",
    )


@cache_page(60 * 30)
def home_view(request):
    return render(
        request=request,
        template_name="home.html"
    )


@login_required(login_url="/admin/login/")
@permission_required("booking_app.view_hotel")
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
        "comments": comments
    }
    return render(
        request=request,
        template_name="comment_user.html",
        context=context
    )


class UserCommentListView(LoginRequiredMixin, ListView):
    login_url = "/admin/login/"
    template_name = "comment_user.html"
    model = HotelsComment
    context_object_name = "comments"
    paginate_by = 20


@cache_page(60 * 30)
@login_required(login_url="/admin/login/")
@permission_required("booking_app.view_person")
def all_apartments(request):
    context = {
        "hotels": Hotel.objects.all().prefetch_related("hotel_comments")
    }
    return render(
        request=request,
        template_name="all_hotel.html",
        context=context
    )


@cache_page(60 * 30)
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


class UserFormView(CreateView):
    template_name = "create_user.html"
    form_class = UserForm
    reverse_lazy = "all_user"


@permission_required("booking_app.view_personcomment", login_url="/admin/login/")
@login_required(login_url="/admin/login/")
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

