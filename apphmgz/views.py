from django.shortcuts import render
from .models import Usuarios


# Create your views here.

def index(request):
    usuario = Usuarios()
    usuario.usuario = "harol.gomez"
    usuario.correo = "hmgomezz@sena.edu.co"
    usuario.clave = "123456"
    usuario.save()
    usuarios = Usuarios.objects.all()
    context = {'usuarios': usuarios}
    return render(request, 'render/index.html', {})
