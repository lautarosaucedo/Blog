from django.db import models

from apps.post.models import post
from apps.usuarios.models import usuarios

class comentarios (models.Model):
    comentario = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    idUsuarios = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    idPost = models.ForeignKey(post, on_delete=models.CASCADE)
    