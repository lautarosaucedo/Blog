from django.contrib import admin

from .models import post , Categoria

class CategoriaList(admin.ModelAdmin):
	list_display = ['id', 'tipo']

admin.site.register(Categoria, CategoriaList)

class postList(admin.ModelAdmin):
	list_display = ['id', 'titulo', 'detalles', 'fecha', 'images']

admin.site.register(post, postList)