from django.db import models

class usuarios (models.Model):
    nombre = models.CharField(max_length = 255)
    apellido = models.CharField(max_length = 255)
    email = models.EmailField(max_length=254)
    telefono = models.IntegerField()
