"""MiPaginaWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from MiPaginaWeb.views import   probandoTemplate, saludo, segunda_vista, diaHoy, miNombre, edad

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/',saludo),
    path("2da/",segunda_vista),   #el nombre del url no tiene que ser el de la función
    path('today/',diaHoy),
    path('name/<nombre>',miNombre),
    path('age/<edad>',edad),
    path('plantilla/',probandoTemplate),
]

