"""
Views para app servicedesk
"""
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

# Create your views here.

def index(request):
    """
    view principal
    """
    return render(request, "email.html")

class EmailView(View):
    """
    View para envio de email
    """
    def get(self, request):
        """
        Implementa requisição HTTP GET
        """
        return HttpResponse("Email enviado com sucesso!")
