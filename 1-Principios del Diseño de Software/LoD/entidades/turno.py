"""
Turno
"""

import datetime

class Turno:


    def __init__(self):
        self._horario = None
        self._paciente = None
        self._aviso = None
        self._estado = None



class Lista_de_Turnos:


    @property
    def lista(self):
        return self._lista

    def __init__(self):
        self._lista = []

    def agregar_turno(self):
        return

    def eliminar_turno(self):
        return



class GestorTurno:

    def __init__(self):
        self._dia_de_turnos = datetime.date.today()
        self._lista_de_turnos = Lista_de_Turnos()


    def notificar_turno(self):

        for turno in self.lista:
            if turno._horario < self.plazo_para_aviso:
                self._enviar_notificacion(turno._paciente.telefono)



