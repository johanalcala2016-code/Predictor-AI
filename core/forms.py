from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import SolicitudPrestamo

class SolicitudPrestamoForm(forms.ModelForm):
    class Meta:
        model = SolicitudPrestamo
        fields = [
            'gender',
            'married',
            'education',
            'applicant_income',
            'coapplicant_income',
            'loan_amount',
            'credit_history',
        ]
        widgets = {
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'married': forms.Select(attrs={'class': 'form-control'}),
            'education': forms.Select(attrs={'class': 'form-control'}),
            'applicant_income': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 5000'}),
            'coapplicant_income': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 2000'}),
            'loan_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto en miles (Ej. 120 para $120,000)'}),
            'credit_history': forms.Select(attrs={'class': 'form-control'}),
        }

# formulario de registro de usuario
class RegistroUsuarioForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre", max_length=30, required=True)
    last_name = forms.CharField(label="Apellido", max_length=30, required=True)
    email = forms.EmailField(label="Correo Electrónico", required=True)

    class Meta:
        model = User
        # Definimos el orden exacto de las casillas en la pantalla:
        fields = ['first_name', 'last_name', 'username', 'email']