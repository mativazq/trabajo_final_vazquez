from django.db import models


class Reserva(models.Model):
    nombre_de_usuario = models.CharField (max_length=50)
    sala = models.CharField(max_length=50)

    del __str__(self):
        return f"Esta es una reserva de {self.nombre_de_usuario} para la sala {self.sala}"

