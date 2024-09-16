from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404
from datetime import datetime


# Create your views here.

def list_page(request):
    
    current_time = datetime.now()

    context_dict = {'boldmessage': "This is my message",
                    'current_time': current_time}
    
    return render(request, 'players/player_list.html', context_dict)

def login(request):
    return render(request, )

def signup(request):
    return HttpResponse("You are now in the sign in view")



