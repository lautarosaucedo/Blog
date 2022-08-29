import email
from django.shortcuts import render
from django.views.generic import TemplateView
from apps.post.models import post
from apps.usuarios.models import usuarios
from apps.comentarios.models import comentarios

def inicio(request):

    return render(request,"inicio.html",{})


"""def login(request):
    
   
        
    return render(request, "login.html", {})
"""
def noticias(request):

    posts = post.objects.all()
    comentarioss = comentarios.objects.all()
    ctx={
        'post' : posts,
        'comentario':comentarioss,
    }
    return render(request, "noticias.html", ctx)
    
def registrar(request):

    return render(request, "registrar.html", {})    
    
