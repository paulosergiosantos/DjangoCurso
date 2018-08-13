
"""
Definição dos Models
"""
from django.db import models

# Create your models here.

class Driver(models.Model):
    """
    Tabela resources_driver
    """
    name = models.CharField(max_length=50, unique=True)
    cnh = models.CharField(max_length=30, unique=True)
    cnh_emissao = models.DateField()

    def __str__(self):
        return ",".join((str(id), str(self.name), str(self.cnh), str(self.cnh_emissao)))

class Manufacturer(models.Model):
    """
    Tabela resources_manufacturer
    """
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    """
    Tabela resources_vehicle
    """
    manufacturer = models.ForeignKey("Manufacturer", on_delete="")
    name = models.CharField(max_length=30, unique=True)
    plate = models.CharField(max_length=8, unique=True)
    usecontrols = models.ManyToManyField(Driver, through="UseControl")

    def __str__(self):
        return ",".join((str(id), str(self.name), str(self.plate), str(self.manufacturer)))

class UseControl(models.Model):
    """
    Tabela resources_usecontrol
    """
    driver = models.ForeignKey(Driver, on_delete="")
    vehicle = models.ForeignKey(Vehicle, on_delete="")
    date_started = models.DateTimeField(auto_now_add=True)
    date_ended = models.DateTimeField(blank=True, null=True)

class User(models.Model):
    """
    Tabela resources_user
    """
    name = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return ",".join((str(id), str(self.name), str(self.phone), str(self.email)))
