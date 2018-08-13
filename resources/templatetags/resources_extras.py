"""
Funcoes extras
"""

from datetime import date, timedelta

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name="calcularIdade")
def calcular_idade(value):
    """
    calcula idade
    """
    today = date.today()
    age = today - value
    return int(age.days / 365)

@register.filter(name="maiusculo")
@stringfilter
def converter_maiusculo(value):
    """
    converte para maiusculo
    """
    return str(value).upper()

@register.filter(name="formatPlaca")
@stringfilter
def formatar_placa(value):
    """
    formata placa para "xxx-0000"
    """
    return str(value)[:3] + '-' + str(value)[3:]

@register.filter(name="calcularTempo")
def calcular_horas(start, end):
    """
    calcula tempo em horas
    """
    diff_hours = 0
    if start and end:
        diff = end - start
        diff_hours = int(diff / timedelta(hours=1))

    return diff_hours

@register.filter(name="calcularTempoUso")
def calcular_tempo_uso(usecontrol):
    """
    calcula tempo em horas
    """
    return calcular_horas(usecontrol.date_started, usecontrol.date_ended)
