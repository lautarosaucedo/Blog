import email
from django.shortcuts import render
from django.views.generic import TemplateView
from apps.post.models import post
from apps.usuarios.models import usuarios

def inicio(request):

    posts = post.objects.all()

    ctx={
        'post' : posts,

    }

    return render(request,"inicio.html",ctx)


"""def login(request):
    
   
        
    return render(request, "login.html", {})
"""
def noticias(request):

    posts = post.objects.all()

    ctx={
        'post' : posts,

    }
    return render(request, "noticias.html", ctx)
    
def registrar(request):

    return render(request, "registrar.html", {})    
    
