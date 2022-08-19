from django.db import models

from usuarios.models import usuarios

class Categoria(models.Model):
	tipo = models.CharField(max_length=255)

	class Meta:
		db_table = 'categorias'

	def __str__(self):
		return self.tipo

	
    
class post (models.Model):
    
    titulo = models.CharField(max_length = 255)
    detalles = models.CharField(max_length = 255)
    fecha = models.TimeField()
    images = models.ImageField(upload_to = "images_post")
    categorias = models.ManyToManyField(Categoria, related_name="categorias")
    idUsuarios = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    



    
