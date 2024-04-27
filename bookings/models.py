from django.db import models



class Sala(models.Model):
    class Tipo(models.TextChoices):
        AUDITORIO = 'AUD', 'Auditorio'
        SALA_DE_CONFERENCIAS = 'CON', 'Sala de Conferencias'
        AULA = 'AUL', 'Aula'
        LABORATORIO = 'LAB', 'Laboratorio'
        
    nombre = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    disponible = models.BooleanField()
    tipo = models.CharField(
        max_length=3,
        choices=Tipo.choices,
        default=Tipo.AULA,
    )

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"