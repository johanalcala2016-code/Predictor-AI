from django.db import models
from django.contrib.auth.models import User

class SolicitudPrestamo(models.Model):
    # Opciones categóricas para los selectores HTML
    GENERO_CHOICES = [
        ('Male', 'Masculino'),
        ('Female', 'Femenino'),
    ]

    ESTADO_CIVIL_CHOICES = [
        ('Yes', 'Casado(a)'),
        ('No', 'Soltero(a)'),
    ]

    EDUCACION_CHOICES = [
        ('Graduate', 'Graduado'),
        ('Not Graduate', 'No Graduado'),
    ]

    # Campos que ingresa el usuario
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENERO_CHOICES, verbose_name="Género")
    married = models.CharField(max_length=3, choices=ESTADO_CIVIL_CHOICES, verbose_name="Estado Civil")
    education = models.CharField(max_length=20, choices=EDUCACION_CHOICES, verbose_name="Nivel Educativo")

    # Resultado de la IA (1 = Aprobado / Y, 0 = Rechazado / N)
    loan_status = models.CharField(max_length=20, default="Pendiente", verbose_name="Estado del Préstamo")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud #{self.id} - {self.gender} | {self.married}"