"""
Instancia de un turno para uso en caso de prueba
"""

from .ejemplo_paciente import fabricar_paciente
from principios.LoD.entidades.turno import *
from datetime import date, time


def fabricar_turno() -> Turno:
    turno = Turno()
    turno.paciente = fabricar_paciente()
    turno.dia = date(2020, 4, 18)
    turno.hora = time(17, 0, 0, 0)
    return turno
