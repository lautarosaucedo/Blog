
from django import forms

from .models import comentarios

class comentarioForm(forms.ModelForm):

	class Meta:
	
		model = comentarios
		fields = ["comentario"]

	