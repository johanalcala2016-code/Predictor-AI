from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import SolicitudPrestamo

class SolicitudPrestamoForm(forms.ModelForm):
    class Meta:
        model = SolicitudPrestamo
        fields = ['gender', 'married', 'education']
        widgets = {
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'married': forms.Select(attrs={'class': 'form-select'}),
            'education': forms.Select(attrs={'class': 'form-select'}),
        }

# formulario de registro de usuario
class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']