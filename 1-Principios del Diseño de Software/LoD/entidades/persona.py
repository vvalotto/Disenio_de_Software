"""
Clase Persona
"""
from datetime import date, datetime

class Persona:

    @property
    def nombres(self):
        return self._nombres

    @nombres.setter
    def nombres(self, valor):
        self._nombres = valor

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        self._apellido = valor

    @property
    def fecha_de_nacimiento(self):
        return self._fecha_de_nacimiento

    @fecha_de_nacimiento.setter
    def fecha_de_nacimiento(self, valor):
        self._fecha_de_nacimiento = valor

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, valor):
        self._genero = valor

    @property
    def documento(self):
        return self._documento

    @documento.setter
    def documento(self, valor):
        self._documento = valor

    @property
    def nombre_y_apellido(self):
        return self._nombres + " " + self._apellido

    @property
    def edad(self):
        return int((date.today() - self._fecha_de_nacimiento).days / 365)

    def __init__(self):
        self._nombres = None
        self._apellido = None
        self._documento = None
        self._fecha_de_nacimiento = None
        self._genero = None

