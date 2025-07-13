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


