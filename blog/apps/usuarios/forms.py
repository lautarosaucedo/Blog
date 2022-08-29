import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import usuarios

class registrarForm(UserCreationForm):

	class Meta:
	
		model = usuarios
		fields = ["first_name", "last_name", "telefono", "email", "username", "password1", "password2"]
