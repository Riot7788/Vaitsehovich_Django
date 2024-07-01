from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    SomeDataView,
    UserApiView,
    OwnerApiView,
    HobbyApiView,
)

urlpatterns = [
    path('some_url', SomeDataView.as_view()),
    path('users', UserApiView.as_view()),
    path('users/<int:pk>', UserApiView.as_view()),
    path('owners', OwnerApiView.as_view()),
    path('owners/<int:pk>', OwnerApiView.as_view()),
    path('hobbyes', HobbyApiView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)