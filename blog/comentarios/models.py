from django.db import models

from post.models import post
from usuarios.models import usuarios

class comentarios (models.Model):
    usuario = models.CharField(max_length = 255)
    comentario = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    fecha = models.TimeField()
    idUsuarios = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    idPost = models.ForeignKey(post, on_delete=models.CASCADE)
    