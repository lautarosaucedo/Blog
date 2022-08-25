from django.urls import reverse
from django.shortcuts import render

from django.views.generic import CreateView

from .models import usuarios
from .forms import postearForm

class postear(CreateView):
	model = usuarios
	template_name = "postear/postear.html"
	form_class = postearForm 

	def get_success_url(self, **kwargs):
		return reverse('noticias')

