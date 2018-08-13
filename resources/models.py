
"""
Definição dos Models
"""
from django.conf import settings
from django.db import models

# Create your models here.

class Driver(models.Model):
    """
    Tabela resources_driver
    """
    class Meta:
        verbose_name = 'Motorista'

    name = models.CharField(max_length=50, unique=True, verbose_name="Nome")
    cnh = models.CharField(max_length=30, unique=True, verbose_name="CNH")
    cnh_emissao = models.DateField(verbose_name="Data emissão CNH")

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    """
    Tabela resources_manufacturer
    """
    class Meta:
        verbose_name = 'Fabricante'

    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    """
    Tabela resources_vehicle
    """
    class Meta:
        verbose_name = 'Veículo'

    manufacturer = models.ForeignKey("Manufacturer", on_delete="", verbose_name="Fabricante")
    name = models.CharField(max_length=30, unique=True, verbose_name="Nome")
    plate = models.CharField(max_length=8, unique=True, verbose_name="Placa")
    usecontrols = models.ManyToManyField(Driver, through="UseControl")

    def __str__(self):
        return ",".join((str(self.name), "Placa: " + str(self.plate)))

class UseControl(models.Model):
    """
    Tabela resources_usecontrol
    """
    driver = models.ForeignKey(Driver, on_delete="", verbose_name="Motorista")
    vehicle = models.ForeignKey(Vehicle, on_delete="", verbose_name="Veículo")
    date_started = models.DateTimeField(auto_now_add=False, verbose_name="Data Início")
    date_ended = models.DateTimeField(blank=True, null=True, verbose_name="Data Entrega")

class User(models.Model):
    """
    Tabela resources_user
    """
    name = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return ",".join((str(self.name), str(self.phone), str(self.email)))

class ManagerControl(models.Model):
    """
    Tabela resources_managercontrol
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete="")
    name = models.CharField(max_length=30)

    def __str__(self):
        return ",".join((self.user.username, str(self.name)))
