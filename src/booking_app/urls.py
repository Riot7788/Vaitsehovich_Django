from django.urls import path


from .views import (
    some_template_view,
    home_view,
    user_view,
    all_apartments,
    comment_user,
    create_user_new,
    all_users,
    feedback_view
)


urlpatterns = [
    path('index', some_template_view),
    path('home', home_view, name="home"),
    path("persons", user_view, name="persons"),
    path('all_hotel', all_apartments, name="hotel"),
    path('comment_user', comment_user, name="comment"),
    path('all_user', all_users, name='all_user'),
    path('create_user/', create_user_new, name='create_user'),
    path('feedback_form/', feedback_view, name='feedback_form'),
]