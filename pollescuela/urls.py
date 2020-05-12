from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from Escuela import forms, views,models
from django.conf.urls import url


urlpatterns = [
    
    path('', include('Escuela.urls')),
    #path('registroescuela/', views.registroescuela, name='registroescuela'),
   
    #path(' ', include('Escuela.urls')),
    #path('', views.registroescuela, name='registroescuela'),
    #path('registroescuela/', views.registroescuela, name='registroescuela'),

    path('admin/', admin.site.urls),
]
