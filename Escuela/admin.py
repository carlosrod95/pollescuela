from django.contrib import admin

# Register your models here.
from .models import Alumno, Gradogrupo
admin.site.register(Alumno)
admin.site.register(Gradogrupo)