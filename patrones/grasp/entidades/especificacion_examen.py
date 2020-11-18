

from .magnitud import *


class Especificacion_Examen:

    def __init__(self, denominacion, material):
        self._denominacion = denominacion
        self._material = material
        self._lista_magnitudes = None
