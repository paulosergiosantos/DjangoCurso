"""
Views para app resources
"""
from django.views.generic.base import TemplateView
from django.shortcuts import render
from resources.models import Driver, User, UseControl

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
    pass

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
        