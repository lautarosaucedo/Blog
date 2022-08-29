from django.db import models

from apps.usuarios.models import usuarios

class Categoria(models.Model):
	tipo = models.CharField(max_length=255)

	class Meta:
		db_table = 'categorias'

	def __str__(self):
		return self.tipo

	
    
class post (models.Model):
    
    titulo = models.CharField(max_length = 255)
    detalles = models.CharField(max_length = 255)
    fecha = models.DateTimeField(auto_now_add= True , null= True)
    images = models.ImageField(upload_to = "images_post")
    categorias = models.ManyToManyField(Categoria, related_name="categorias")
    
    



    
