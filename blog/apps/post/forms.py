
from .models import post

from django import forms

class postearForm(forms.ModelForm):

	class Meta:
	
		model = post
		fields = ["titulo", "detalles", "images", "categorias"]