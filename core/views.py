from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def contactanos(request):
    return render(request, 'core/contactanos.html')

def Suscripcion(request):
    return render(request, 'core/Suscripcion.html')


def iniciosesion(request):
    return render(request, 'core/iniciosesion.html')

def registro(request):
    return render(request, 'core/registro.html')

def Bandanas(request):
    return render(request, 'core/Bandanas.html')

def collares(request):
    return render(request, 'core/collares.html')

def correas(request):
    return render(request, 'core/correas.html')

def identificaciones(request):
    return render(request, 'core/identificaciones.html')
