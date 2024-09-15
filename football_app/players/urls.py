from django.urls import path
from players import views


app_name = 'players'

urlpatterns = [
path('', views.list_page, name='list_page'),
path('signup', views.signup, name="signup"),
path('login', views.login, name='login'),

]

