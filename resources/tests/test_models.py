
"""
Testes unitários models
"""

from django.test import TestCase

from resources.models import Driver, User

# Create your tests here.

class DriverTestCase(TestCase):
    """
    Teste unidade Driver
    """
    def setUp(self):
        Driver.objects.create(name="Joao", cnh="0101", cnh_emissao="1990-01-01")

    def test_drive(self):
        """
        Teste Driver
        """
        driver = Driver.objects.get(name="Joao")
        self.assertEqual("Joao", driver.name)
        self.assertEqual("0101", driver.cnh)

class UserTestCase(TestCase):
    """
    Teste unidade User
    """
    def setUp(self):
        User.objects.create(name="Joao", phone="99998888", email="joao@inatel.br")

    def test_user(self):
        """
        Teste User
        """
        user = User.objects.get(name="Joao")
        self.assertEqual("Joao", user.name)
        self.assertEqual("99998888", user.phone)
        self.assertEqual("joao@inatel.br", user.email)
