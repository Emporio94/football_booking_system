from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404
from datetime import datetime, timedelta



# Create your views here.

def hours_until_friday_10am():
    now = datetime.now()
    days_ahead = 4 - now.weekday()

    if days_ahead < 0 or (days_ahead == 0 and now.hour >= 10):
        days_ahead += 7

    next_friday_10am = (now + timedelta(days=days_ahead)).replace(hour=10, minute=0, second=0, microsecond=0)
    time_difference = next_friday_10am - now
    hours_left = time_difference.total_seconds() / 3600

    return round(hours_left)

def list_page(request):
    
    current_time = datetime.now()

    context_dict = {'boldmessage': "This is my message",
                    'current_time': hours_until_friday_10am()}
    
    return render(request, 'players/player_list.html', context_dict)

def login(request):
    return render(request, 'players/login.html')

def signup(request):
    return render(request, 'players/signup.html')



