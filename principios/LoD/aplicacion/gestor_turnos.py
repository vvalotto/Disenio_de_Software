

from entidades.turno import *
from entidades.paciente import *


class GestorTurno:

    def __init__(self):
        self._turno_del_dia = None

    def crear_lista_de_turnos(self):
        self._dia_de_turnos = datetime.date.today()
        self._lista_de_turnos = Lista_de_Turnos()
        return

    def dar_turno(self):
        paciente = self._ingresar_paciente()
        horario = self._asignar_horario()
        self._agregar_turno(paciente, horario)
        return

    def generar_notificaciones_para_turnos(self):
        return

    def notificar_turno(self):

        for turno in self.lista:
            if turno._horario < self.plazo_para_aviso:
                self._enviar_notificacion(turno._paciente.telefono)

    def _ingresar_paciente(self):
        paciente = Paciente()

        paciente.nombres = ""
        paciente.apellido = ""
        paciente.fecha_de_nacimiento = ""
        paciente.obra_social_nombre = ""
        paciente.obra_social_id = ""

        return paciente

    def _asignar_horario(self):
        horario = None
        return horario

    def _agregar_turno(self, paciente, horario):
        return