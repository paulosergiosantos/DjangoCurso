"""
Mapeamento das urls
"""
from django.conf.urls import url

from resources.views import UseControlView

from . import views

urlpatterns = [
    url(r'^resources', views.index, name='index'),
    url(r'^usuarios', views.usuarios, name='usuarios'),
    url(r'^veiculos', views.veiculos, name='veiculos'),
    url(r'^motoristas', views.motoristas, name='motoristas'),
    url(r'^usecontrol', UseControlView.as_view()),
]
