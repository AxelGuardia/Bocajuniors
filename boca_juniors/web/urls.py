from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar-novedades/', views.agregar_novedades, name='agregar_novedades'),
    path('buscar-novedades/', views.buscar_novedades, name='buscar_novedades'),
]
