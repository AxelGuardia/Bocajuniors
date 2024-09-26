from django.shortcuts import render, redirect
from .forms import NovedadesForm, FutbolForm, IndumentariaForm
from .models import Novedades, Futbol, Indumentaria

def home(request):
    return render(request, 'web/home.html')

def agregar_novedades(request):
    if request.method == 'POST':
        form = NovedadesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NovedadesForm()
    return render(request, 'web/formulario.html', {'form': form, 'titulo': 'Agregar Novedades'})

def buscar_novedades(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        resultados = Novedades.objects.filter(titulo__icontains=query)
        return render(request, 'web/resultados.html', {'resultados': resultados, 'titulo': 'Resultados de Novedades'})
    return render(request, 'web/buscar.html', {'titulo': 'Buscar Novedades'})
