from django.db import models
from django.contrib.auth.models import AbstractUser



class usuarios (AbstractUser):
	telefono = models.CharField(max_length=255, null=True, blank=True)
	apellido = models.CharField(max_length=255, null=True, blank=True)
	nombre = models.CharField(max_length=255, null=True, blank=True)
    



    
   
    
   
   