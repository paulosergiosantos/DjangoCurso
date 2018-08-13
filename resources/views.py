"""
Views para app resources
"""
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from resources.models import Driver, UseControl, User, Vehicle

# Create your views here.

def index(request):
    """
    view principal
    """
    return render(request, "hello.html")

def usuarios(request):
    """
    view usuarios
    """

    users = User.objects.raw('SELECT id, name, phone, email FROM resources_user')
    users = {"users": users}
    return render(request, "usuarios.html", users)

def veiculos(request):
    """
    view veiculos
    """
    return render(request, "veiculos.html")

def motoristas(request):
    """
    view motoristas
    """
    drivers = Driver.objects.all()
    drivers = {"drivers": drivers}
    return render(request, "motoristas.html", drivers)

def usecontrol_add(request):
    """
    adiciona entra na tabela usecontrol
    """

def usecontrol_list(request):
    """
    view usecontrol
    """
    usecontrols = UseControl.objects.all()
    usecontrols = {"usecontrols": usecontrols}
    return render(request, "usecontrol_list.html", usecontrols)

class UseControlView(TemplateView):
    """
    View usecontrol com template
    """
    template_name = "usecontrol_list.html"

    def get_context_data(self, **kwargs):
        context = super(UseControlView, self).get_context_data(**kwargs)
        context["usecontrols"] = UseControl.objects.all()
        return context

class VehicleCreateView(CreateView): # pylint: disable=too-many-ancestors
    """
    View para tratar HTTP POST para veiculo
    """
    model = Vehicle
    template_name = "vehicle_form.html"
    fields = ["name", "plate", "manufacturer"]

    def get_success_url(self):
        return reverse('vehicle_list')


class VehicleUpdateView(UpdateView): # pylint: disable=too-many-ancestors
    """
    View para tratar HTTP PUT para veiculo
    """
    model = Vehicle
    template_name = "vehicle_form.html"
    fields = ["name", "plate", "manufacturer"]
    def get_success_url(self):
        return reverse('vehicle_list')

class VehicleDeleteView(DeleteView): # pylint: disable=too-many-ancestors
    """
    View para tratar HTTP DELETE para veiculo
    """
    model = Vehicle
    template_name = "vehicle_confirm_delete.html"
    def get_success_url(self):
        return reverse('vehicle_list')

class VehicleListView(ListView): # pylint: disable=too-many-ancestors
    """
     View para tratar HTTP GET para veiculo
    """
    model = Vehicle
    template_name = "vehicle_list.html"
    queryset = Vehicle.objects.order_by("plate")
