from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
import os
import joblib
import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SolicitudPrestamoForm, RegistroUsuarioForm
from .models import SolicitudPrestamo

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'modelo.pkl')
model = joblib.load(MODEL_PATH)

def registro(request):
    """Vista para registrar nuevos usuarios"""
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def home(request):
    """Página principal con historial"""
    # Si el usuario está autenticado, muestra solo sus solicitudes; si no, todas o ninguna
    if request.user.is_authenticated:
        solicitudes = SolicitudPrestamo.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    else:
        solicitudes = SolicitudPrestamo.objects.all().order_by('-fecha_creacion')
    return render(request, 'core/home.html', {'solicitudes': solicitudes})

@login_required  # Requiere que el usuario esté logueado

def crear_solicitud(request):
    """Procesa el formulario y ejecuta la SIMULACIÓN de la IA"""
    if request.method == 'POST':
        form = SolicitudPrestamoForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            if request.user.is_authenticated:
                solicitud.usuario = request.user
            
# -------------------------------------------------------------
            # INTEGRACIÓN CON LA IA REAL (Integración Final - C1)
            # -------------------------------------------------------------
            # 1. Mapeo de
            applicant_income = form.cleaned_data.get('applicant_income', 0)
            coapplicant_income = form.cleaned_data.get('coapplicant_income', 0)
            loan_amount = form.cleaned_data.get('loan_amount', 0) 
            # Extraemos la opción seleccionada (0, 1 o 2)
            credit_history_raw = int(form.cleaned_data['credit_history'])
            
            # Mapeo: Si eligió 0 (Malo) o 2 (Sin historial), mandamos 0 a la IA. Si eligió 1 (Bueno), mandamos 1.
            credit_history_ia = 0 if credit_history_raw in [0, 2] else 1
        
            # 2. Construir el vector de entrada exacto
            input_ia = pd.DataFrame([{
                'ApplicantIncome': applicant_income,
                'CoapplicantIncome': coapplicant_income,
                'LoanAmount': loan_amount,
                'Credit_History': credit_history_ia,  # <--- Usamos esta variable
            }])

            # 3. Predicción con el modelo real cargado
            prediccion = model.predict(input_ia)[0]

            # 4. Asignar resultado (1 = Aprobado, 0 = Rechazado)
            if prediccion in [1, '1', 'Y', 'Yes']:
                solicitud.loan_status = 'Aprobado'
            else:
                solicitud.loan_status = 'Rechazado'

            solicitud.save()
            return redirect('detalle_solicitud', pk=solicitud.pk)
            # Redirigimos a la pantalla con el resultado detallado
    else:
        form = SolicitudPrestamoForm()
        
    return render(request, 'core/formulario.html', {'form': form})

def detalle_solicitud(request, pk):
    """Muestra la tarjeta de dictamen final de una solicitud específica"""
    solicitud = get_object_or_404(SolicitudPrestamo, pk=pk)
    return render(request, 'core/detalle.html', {'solicitud': solicitud})

def login_view(request):
    """Vista personalizada para inicio de sesión"""
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        
        user = authenticate(request, username=u, password=p)
        
        if user is not None:
            auth_login(request, user)
            # Redirige a la URL previa ('next') o al 'home'
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
            
    return render(request, 'usuarios/login.html')