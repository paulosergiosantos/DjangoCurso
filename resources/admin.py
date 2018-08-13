"""
Configuração do site admin
"""
from django.contrib import admin

from .models import (Driver, ManagerControl, Manufacturer, UseControl, User,
                     Vehicle)

# Register your models here.

class DriverAdmin(admin.ModelAdmin):
    """
    DriverAdmin
    """
    list_display = ('name', 'cnh', 'cnh_emissao')

class VechicleAdmin(admin.ModelAdmin):
    """
    VechicleAdmin
    """
    list_display = ('name', 'plate', 'manufacturer')
    list_per_page = 5

class UseControlAdmin(admin.ModelAdmin):
    """
    DriUseControlAdmin
    """
    list_display = ('driver', 'vehicle', 'date_started', 'date_ended')

class ManufacturerAdmin(admin.ModelAdmin):
    """
    ManufacturerAdmin
    """
    pass

class UserAdmin(admin.ModelAdmin):
    """
    UserAdmin
    """
    pass

class ManagerControlAdmin(admin.ModelAdmin):
    """
    ManagerControlAdmin
    """
    list_display = ('user', 'name')

admin.site.register(Driver, DriverAdmin)
admin.site.register(ManagerControl, ManagerControlAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(UseControl, UseControlAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Vehicle, VechicleAdmin)
