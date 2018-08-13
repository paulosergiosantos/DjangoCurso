"""
Veiculos template tags
"""
import sqlite3
from sqlite3 import Error

from django import template

from fleet_control.settings import DATABASES
from resources.models import Vehicle

register = template.Library()

def create_connection():
    """
    criar conexão com a base sqlite3
    """
    default = DATABASES["default"]
    db_file = default["NAME"]
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as ex:
        print(ex)

    return None

def select_all_vehicles():
    """
    selecionar todos os veiculos
    """
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM resources_vehicle")
    rows = cur.fetchall()

    conn.close()

    return rows

@register.simple_tag
def get_vehicles_sql(number_items):
    """
    lista veiculos com sql nativa
    """
    vehicles = select_all_vehicles()
    vehicles = [Vehicle(row[0], row[1], row[2]) for row in vehicles]
    return vehicles[:number_items]

@register.simple_tag
def get_vehicles():
    """
    lista veiculos com uso do framework django
    """
    vehicles = Vehicle.objects.all()
    return vehicles
