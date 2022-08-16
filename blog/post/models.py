from django.db import models

class post (models.Model):
    titulo = models.CharField(max_length = 255)
    detalles = models.CharField(max_length = 255)
    categoria = models.CharField(max_length = 255)
    fecha = models.TimeField()
