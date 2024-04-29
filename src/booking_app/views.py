from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_view(request):
    return HttpResponse("<h1>Hello django app</h1>")

def all_apartment(request):
    return HttpResponse("<h1>All apartment rent</h1>")