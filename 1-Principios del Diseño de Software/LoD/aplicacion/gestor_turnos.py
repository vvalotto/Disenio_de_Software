

from entidades.turno import *


class GestorTurno:

    def __init__(self):
        self._turno_del_dia = None

    def crear_lista_de_turnos(self):
        self._turnos_del_dia = Lista_de_Turnos()
        return

    def dar_turno(self):
        paciente = self._ingresar_paciente()
        horario = self._asignar_horario()
        self._agregar_turno(paciente, horario)
        return

    def generar_notificaciones_para_turnos(self):
        return

    def _ingresar_paciente(self):
        paciente = None
        return paciente

    def _asignar_horario(self):
        horario = None
        return horario

    def _agregar_turno(self, paciente, horario):
        return