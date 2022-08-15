from django.db import models

class post (models.Model):
    titulo = models.CharField(max_length = 255)
    

