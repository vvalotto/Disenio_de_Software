

from entidades.turno import *
from entidades.paciente import *


class GestorTurno:

    @property
    def lista_de_turnos(self):
        return self._lista_de_turnos.lista

    def __init__(self):
        self._dia_de_turnos = datetime.today()
        self._lista_de_turnos = ListaDeTurnos()

    def dar_turno(self, paciente, dia, hora):
        turno = Turno()
        turno.dia = dia
        turno.hora = hora
        turno.paciente = paciente
        self._lista_de_turnos.agregar_turno(turno)

    def notificar_turno(self, plazo_notificacion):
        for turno in self._lista_de_turnos.lista:
            print(str(turno.hora))
            '''  
            if turno.evento -  < plazo_notificacion:
                self._enviar_notificacion(turno._paciente.telefono)
            '''
