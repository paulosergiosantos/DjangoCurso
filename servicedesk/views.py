"""
Views para app servicedesk
"""
from django.shortcuts import render

# Create your views here.

def index(request):
    """
    view principal
    """
    return render(request, "email.html")
