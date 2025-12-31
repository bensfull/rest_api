from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_users, name="get_all_users" ),
    path('user/<str:nick>/', views.get_by_nick, name='get_by_name'),
    path('data/', views.user_manager)
    
]
