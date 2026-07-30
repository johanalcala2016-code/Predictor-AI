from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nueva-solicitud/', views.crear_solicitud, name='crear_consulta'),
    path('solicitud/<int:pk>/', views.detalle_solicitud, name='detalle_solicitud'),

    # Rutas de Autenticación
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]