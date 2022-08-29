from django.db import models

from apps.post.models import post
from apps.usuarios.models import usuarios

class comentarios (models.Model):
    comentario = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add= True , null= True)
   
    