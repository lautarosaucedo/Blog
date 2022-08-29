from django.urls import path 

from . import views

app_name = "post"

urlpatterns = [

    path("postear/", views.postearC.as_view(), name="postear"),
]