from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola mundo desde Django")

from django.http import HttpResponse

def primera_pagina(request):
    return HttpResponse("¡Bienvenido a EnsaladaDeFrutas!")

def fruta_por_id(request, fruta_id):
    return HttpResponse(f"Mostrando fruta con ID: {fruta_id}")

# vista

from django.shortcuts import render, redirect, get_object_or_404
from .models import Fruta, Usuario

def fruta_list(request):
    frutas = Fruta.objects.all()
    return render(request, 'fruta_list.html', {'frutas': frutas})

def fruta_create(request):
    if request.method == 'POST':
        Fruta.objects.create(
            nombre=request.POST['nombre'],
            color=request.POST['color'],
            tipo=request.POST['tipo'],
            descripcion=request.POST['descripcion']
        )
        return redirect('fruta_list')
    return render(request, 'fruta_form.html')

def fruta_update(request, id):
    fruta = get_object_or_404(Fruta, id=id)
    if request.method == 'POST':
        fruta.nombre = request.POST['nombre']
        fruta.color = request.POST['color']
        fruta.tipo = request.POST['tipo']
        fruta.descripcion = request.POST['descripcion']
        fruta.save()
        return redirect('fruta_list')
    return render(request, 'fruta_form.html', {'fruta': fruta})

def fruta_delete(request, id):
    fruta = get_object_or_404(Fruta, id=id)
    fruta.delete()
    return redirect('fruta_list')

