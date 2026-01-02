from django.contrib import admin
from django.urls import path

from . import views


from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('', views.get_users, name="get_all_users" ),
    path('user/<str:nick>/', views.get_by_nick, name='get_by_name'),
    path('data/', views.user_manager),
        
    # 1. O arquivo que contém os dados da sua API (o "contrato")
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    
    # 2. A página bonitinha que você vai abrir no navegador
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    path('criar_post', views.create_post, name='cria_post'),
        
]
