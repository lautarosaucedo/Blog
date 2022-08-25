from django.urls import path 

from . import views

app_name = "registrar"

urlpatterns = [

    path('registrarse/', views.registrar.as_view()),

]