"""
Testes unitários resources extras
"""

from datetime import date
from datetime import datetime

from django.test import TestCase

from resources.templatetags.resources_extras import (calcular_idade,
                                                     calcular_horas,
                                                     converter_maiusculo,
                                                     formatar_placa)


class ResourcesExtrasTestCase(TestCase):
    """
    Teste para resources extras
    """
    def setUp(self):
        pass

    def test_converter_maiusculo(self):
        """
        Teste conveter para maiusculo
        """
        upper = converter_maiusculo("abc")
        self.assertEqual("ABC", upper)

    def test_formatar_placa(self):
        """
        Teste calcular idade
        """
        plate = formatar_placa("PUZ0362")
        self.assertEqual("PUZ-0362", plate)

    def test_calcular_idade(self):
        """
        Teste calcular idade
        """
        birthday = date(1990, 1, 1)
        age = calcular_idade(birthday)
        self.assertEqual(28, age)

    def test_calcular_tempo(self):
        """
        Teste calcular tempo
        """
        start = datetime(2018, 8, 6, 12, 50, 0)
        end = datetime(2018, 8, 8, 12, 50, 0)
        diff = calcular_horas(start, end)
        self.assertEqual(48, diff)
        