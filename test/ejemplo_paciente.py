"""
Instancia de Paciente para uso en caso de prueba
"""

from principios.LoD.entidades.paciente import *
import datetime


def fabricar_paciente() -> Paciente:
    paciente = Paciente()
    paciente.nombres = "Alejo Antonio"
    paciente.apellido = "Valotto"
    paciente.fecha_de_nacimiento = datetime.date(2009, 4, 23)
    paciente.obra_social_id = 1
    paciente.obra_social_nombre = "OSUNER"
    return paciente
