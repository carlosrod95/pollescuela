from django.urls import path,re_path
from . import views

from django.contrib.auth.views import LoginView, LogoutView
from Escuela import forms, views,models
from datetime import datetime

  
urlpatterns = [
    path('', views.home, name='home'),
    #re_path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('consulta_alumno/', views.consulta_alumno, name='ConAlumno'),
   
    path('login/',
         LoginView.as_view
         (
             template_name='Escuela/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]