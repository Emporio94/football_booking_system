from django.contrib import admin
from django.urls import path
from django.urls import include
from players import views

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.list_page, name="list_page"),
    path('players/', include('players.urls')),
]
