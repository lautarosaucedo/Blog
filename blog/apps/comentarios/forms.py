
from django import forms
from .models import comentarios

from django import forms

class comentarioForm(forms.ModelForm):

	class Meta:
	
		model = comentarios
		fields = ["comentario"]

	