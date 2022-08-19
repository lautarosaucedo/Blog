from django.db import models


CARGOS_CHOICES = (
	("A", "ADMIN"),
	("V", "VISITANTE")
)

class usuarios (models.Model):
    nombre = models.CharField(max_length = 255)
    apellido = models.CharField(max_length = 255)
    email = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=254)
    contraseña = models.CharField(max_length=254)
    usuarios = models.CharField(max_length=254)
    tipoUsuario = models.CharField(max_length=1, choices=CARGOS_CHOICES, default="V")


