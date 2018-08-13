"""
Mapeamento das urls
"""
from django.conf.urls import url

from resources.views import UseControlView

from . import views
from .views import VehicleCreateView, VehicleDeleteView, VehicleUpdateView, VehicleListView

urlpatterns = [
    url(r'^resources', views.index, name='index'),
    url(r'^usuarios', views.usuarios, name='usuarios'),
    url(r'^veiculos/$', views.veiculos, name='veiculos'),
    url(r'^motoristas', views.motoristas, name='motoristas'),
    url(r'^usecontrol', UseControlView.as_view()),

    url(r'^veiculos/list$', VehicleListView.as_view(), name='vehicle_list'),
    url(r'^veiculos/add/$', VehicleCreateView.as_view(), name='vehicle_add'),
    url(r'^veiculos/(?P<pk>\d+)/$', VehicleUpdateView.as_view(), name='vehicle_update'),
    url(r'^veiculos/(?P<pk>\d+)/delete/$', VehicleDeleteView.as_view(), name='vehicle_delete'),
]
