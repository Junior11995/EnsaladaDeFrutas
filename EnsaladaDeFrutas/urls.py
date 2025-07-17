"""
URL configuration for EnsaladaDeFrutas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from selector.views import saludo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', saludo),  
]

from django.contrib import admin
from django.urls import path
from selector.views import primera_pagina

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', primera_pagina),  # Página principal
]
from selector.views import fruta_por_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', primera_pagina),
    path('fruta/<int:fruta_id>/', fruta_por_id),  # Ruta con parámetro
]

from django.urls import path
from selector import views

urlpatterns = [
    path('', views.primera_pagina, name='inicio'),
    path('frutas/', views.fruta_list, name='fruta_list'),
    path('frutas/crear/', views.fruta_create, name='fruta_create'),
    path('frutas/<int:id>/editar/', views.fruta_update, name='fruta_update'),
    path('frutas/<int:id>/eliminar/', views.fruta_delete, name='fruta_delete'),

    path('usuarios/', views.usuario_list, name='usuario_list'),
    path('usuarios/crear/', views.usuario_create, name='usuario_create'),
    path('usuarios/<int:id>/editar/', views.usuario_update, name='usuario_update'),
    path('usuarios/<int:id>/eliminar/', views.usuario_delete, name='usuario_delete'),
]


