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

    HISTORIAL_CHOICES = [
        (1, 'Buen historial (Pagos al día / Líneas activas)'),
        (0, 'Malo (Historial crediticio negativo)'),
        (2, 'Sin historial crediticio (Primera vez)'),  # Se mapeará a 0 en la vista
    ]

    # Campos de relación y personales
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENERO_CHOICES, verbose_name="Género")
    married = models.CharField(max_length=3, choices=ESTADO_CIVIL_CHOICES, verbose_name="Estado Civil")
    education = models.CharField(max_length=20, choices=EDUCACION_CHOICES, verbose_name="Nivel Educativo")

    # Campos Financieros (Necesarios para la IA)
    applicant_income = models.IntegerField(default=0, verbose_name="Ingreso del Solicitante")
    coapplicant_income = models.FloatField(default=0.0, verbose_name="Ingreso del Co-solicitante")
    loan_amount = models.IntegerField(default=0, verbose_name="Monto del Préstamo (en miles)")
    credit_history = models.IntegerField(choices=HISTORIAL_CHOICES, default=1, verbose_name="Historial Crediticio")

    # Resultado de la IA (Aprobado / Rechazado / Pendiente)
    loan_status = models.CharField(max_length=20, default="Pendiente", verbose_name="Estado del Préstamo")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        nombre_usuario = self.usuario.username if self.usuario else "Anónimo"
        return f"Solicitud #{self.id} - {nombre_usuario} ({self.loan_status})"