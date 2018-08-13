"""fleet_control URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from resources import views

urlpatterns = [
    url('servicedesk/', include('servicedesk.urls')),
    url('frota/', include('resources.urls')),
    path('', views.index),
    path('frota/', views.index),
    path('admin/', admin.site.urls),
    #path('frota/resources/', views.index),
    #path('frota/veiculos/', views.veiculos),
    #path('frota/usuarios/', views.usuarios),
    #path('frota/motoristas/', views.motoristas),
]
