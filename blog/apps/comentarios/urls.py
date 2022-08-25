from django.urls import path 

from .import views

app_name = "comentario"

urlpatterns = [

    path('comentario/', views.comentar.as_view()),

]