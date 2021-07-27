from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contactanos', views.contactanos, name="contactanos"),
    path('Suscripcion', views.Suscripcion, name="Suscripcion"),
    path('iniciosesion', views.iniciosesion, name="iniciosesion"),
    path('registro', views.registro, name="registro"),
    path('Bandanas', views.Bandanas, name="Bandanas"),
    path('collares', views.collares, name="collares"),
    path('correas', views.correas, name="correas"),
    path('identificaciones', views.identificaciones, name="identificaciones"),
    
]