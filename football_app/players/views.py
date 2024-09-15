from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404

# Create your views here.

def list_page(request):
    return HttpResponse("You are now on the list_page review")

def login(request):
    return HttpResponse("You are now in the login view")

def signup(request):
    return HttpResponse("You are now in the sign in view")



