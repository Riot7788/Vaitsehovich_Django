from django.urls import path
from .views import (
    some_template_view,
    home_view,
    user_view,
    all_apartments,
    comment_user,
)


urlpatterns = [
    path('index', some_template_view),
    path('home', home_view, name="home"),
    path("persons", user_view, name="persons"),
    path('all_hotel', all_apartments, name="hotel"),
    path('comment_user', comment_user, name="comment"),
]