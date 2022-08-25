from django.urls import path 

from . import views

app_name = "postear"

urlpatterns = [

    path('postear/', views.postear.as_view())
]