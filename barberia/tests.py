import unittest
from django.test import TestCase
from models import Turno
import os
import django
import os
import sys

# Agrega la ruta del proyecto Django a sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "barberia.settings")
django.setup()

class TestTurno(unittest.TestCase):
    def test_turno_creation(self):
        turno = Turno(12/10/2023, "Barberia", "Corte Simple", "tizi", 13.00)
        self.assertEqual(turno.fecha, 12/10/2023)
        self.assertEqual(turno.especialidad, "Barberia")
        self.assertEqual(turno.servicio, "Corte Simple")
        self.assertEqual(turno.profesional, "tizi")
        self.assertEqual(turno.hora, 13.00)


