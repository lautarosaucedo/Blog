from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse

from .forms import postearForm
from .models import usuarios

class postearC(CreateView):
	model = usuarios
	template_name = "postear/postear.html"
	form_class = postearForm 

	def get_success_url(self, **kwargs):
		return reverse('noticias')

