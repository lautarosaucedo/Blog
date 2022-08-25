import email
from django import forms

from .models import usuarios

class registrarForm(forms.ModelForm):

	class Meta:
	
		model = usuarios
		fields = ["nombre", "apellido", "telefono", "email", "username", "password"]

	