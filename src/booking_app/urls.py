
from django.urls import path
from .views import first_view
from .views import all_apartment
urlpatterns = [
    path('first_url', first_view),
    path('all_apartment', all_apartment)
]