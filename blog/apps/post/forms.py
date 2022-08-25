import email
from django import forms

from .models import post

class postearForm(forms.ModelForm):

	class Meta:
	
		model = post
		fields = ["titulo", "detalles", "images"]