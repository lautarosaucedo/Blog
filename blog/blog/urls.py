
from email.mime import base
from threading import local
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name = "inicio"),
    
    path('iniciar-seccion/', auth_views.LoginView.as_view(template_name="login.html"), name = "login"),
    path('cerrar-seccion/',auth_views.logout_then_login, name="logout"),
   
    path('noticias/', views.noticias, name="noticias"),

    path('registrar/',include('apps.usuarios.urls')),  
    path('comentar/',include('apps.comentarios.urls')),
    path('postear/',include('apps.post.urls')),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



