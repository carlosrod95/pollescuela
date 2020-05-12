"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import Alumno, Gradogrupo

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
class AlumnoForm(forms.Form):
    nombre = forms.CharField(max_length=30,label='Nombre')
    appaterno = forms.CharField(max_length=30,label='Apellido Paterno')
    apmaterno = forms.CharField(max_length=30,label='Apellido Materno')
    curp = forms.CharField(max_length=18, label='CURP')
    tutor = forms.CharField(max_length=40, label='Tutor')
    matricula= forms.CharField(max_length=10, label='Numero de Matricula')
    Sexo = forms.CharField(max_length=1,label='Sexo M o F')
    fecha_nacimiento= forms.DateField(label='Fecha Nacimiento')
