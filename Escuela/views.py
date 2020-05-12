
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .forms import AlumnoForm 
from .models import Alumno

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'Escuela/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'Escuela/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'Escuela/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def consulta_alumno(request):
    assert isinstance(request, HttpRequest)
    alumnosdata=Alumno.objects.all()
    
    return render(
        request,
        'Escuela/consulta_alumno.html',context= {
        "lista_alumnos":alumnosdata,
            'title':'registroescuela',
            'year':datetime.now().year,
           'message':'Your application description page.',
        },
        
    )