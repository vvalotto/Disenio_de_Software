from unittest import TestCase
from principios.LoD.aplicacion.gestor_turnos import *
from .ejemplo_paciente import *
from datetime import date, time

class TestGestorTurno(TestCase):

    def setUp(self) -> None:
        '''
        self._gestor_de_turnos.dar_turno(fabricar_paciente(), datetime(2020, 4, 19), datetime.time(15, 0, 0))
        self._gestor_de_turnos.dar_turno(fabricar_paciente_2(), datetime(2020, 4, 19), datetime.time(14, 0, 0))
        self._gestor_de_turnos.dar_turno(fabricar_paciente_3(), datetime(2020, 4, 19), datetime.time(14, 30, 0))
        '''

    def test_dar_turno(self):
        self._gestor_de_turnos = GestorTurno()
        self._gestor_de_turnos.dar_turno(fabricar_paciente(), date(2020, 4, 18), time(17, 0, 0, 0))
        self._gestor_de_turnos.notificar_turno(30)
        self.assertEqual(len(self._gestor_de_turnos.lista_de_turnos), 1)

    def test_notificar_turno(self):

        self.assertEqual(0, 0)
