from django.shortcuts import render

from post.models import post
from usuarios.models import usuarios

def inicio(request):

    posts = post.objects.all()

    ctx={
        'post' : posts,

    }

    return render(request,"inicio.html",ctx)


def login(request):
    return render(request, "login.html", {})

def noticias(request):
    return render(request, "noticias.html", {})
    
def registrar(request):
    return render(request, "registrar.html", {})    