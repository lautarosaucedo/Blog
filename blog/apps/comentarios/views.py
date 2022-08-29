from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse

from .models import comentarios, usuarios
from .forms import comentarioForm

class comentar(CreateView):
	model = comentarios
	template_name = "comentar/comentar.html"
	form_class = comentarioForm 

	def get_success_url(self, **kwargs):
		return reverse('noticias')
