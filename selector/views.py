from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Fruta, Usuario
from .forms import UsuarioForm, FrutaForm  # Asegúrate de tener forms.py creado

# Página de saludo
def saludo(request):
    return HttpResponse("Hola mundo desde Django")

# Página principal
def primera_pagina(request):
    return HttpResponse("¡Bienvenido a EnsaladaDeFrutas!")

# Vista de fruta por ID
from django.http import Http404

def fruta_por_id(request, fruta_id):
    try:
        fruta = Fruta.objects.get(id=fruta_id)
    except Fruta.DoesNotExist:
        raise Http404("Fruta no encontrada.")
    return HttpResponse(f"Fruta: {fruta.nombre}, Color: {fruta.color}, Tipo: {fruta.tipo}")


# CRUD para Fruta
def fruta_list(request):
    frutas = Fruta.objects.all()
    return render(request, 'fruta_list.html', {'frutas': frutas})

def fruta_create(request):
    form = FrutaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fruta_list')
    return render(request, 'fruta_form.html', {'form': form})

def fruta_update(request, id):
    fruta = get_object_or_404(Fruta, id=id)
    form = FrutaForm(request.POST or None, instance=fruta)
    if form.is_valid():
        form.save()
        return redirect('fruta_list')
    return render(request, 'fruta_form.html', {'form': form})

def fruta_delete(request, id):
    fruta = get_object_or_404(Fruta, id=id)
    fruta.delete()
    return redirect('fruta_list')

# CRUD para Usuario
def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario_list.html', {'usuarios': usuarios})

def usuario_create(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('usuario_list')
    return render(request, 'usuario_form.html', {'form': form})

def usuario_update(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    form = UsuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('usuario_list')
    return render(request, 'usuario_form.html', {'form': form})

def usuario_delete(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect('usuario_list')

