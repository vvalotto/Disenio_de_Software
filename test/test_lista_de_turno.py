from unittest import TestCase
from principios.LoD.entidades.turno import Lista_de_Turnos
from .ejemplo_turno import fabricar_turno


class TestLista_de_Turnos(TestCase):

    def setUp(self) -> None:
        self._turno = fabricar_turno()
        self._lista_de_turnos = Lista_de_Turnos()

    def test_lista_vacia(self):
        self.assertEqual(len(self._lista_de_turnos.lista), 0)

    def test_agregar_turno(self):
        self._lista_de_turnos.agregar_turno(self._turno)
        self.assertEqual(len(self._lista_de_turnos.lista), 1)

    def test_hay_horario_ocupado(self):
        self.assertEqual(self._lista_de_turnos.hay_horario_ocupado(self._turno.hora), 0)

    def test_eliminar_turno(self):
        self._lista_de_turnos.eliminar_turno(self._turno)
        self.assertEqual(len(self._lista_de_turnos.lista), 0)

    def test_ordenar_por_horario(self):
        self.assertEqual(0, 0)
