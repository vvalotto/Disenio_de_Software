class ValorReferencia:

    def __init__(self, descripcion, valor):
        self._descripcion = descripcion
        self._valor = valor

    def __str__(self):
        return self._descripcion + ":" + str(self._valor)


class Magnitud:

    @property
    def unidad_de_medida(self):
        return self._unidad_de_medida

    @property
    def valores_referencia(self):
        return self._valores_referencia

    def __init__(self, descripcion, unidades_de_medida):
        self._descripcion = descripcion
        self._valores_referencia = []
        self._unidad_de_medida = unidades_de_medida

    def agregar_valor_referencia(self, valor_referencia):
        self._valores_referencia.append(valor_referencia)

    def __str__(self):
        return self._descripcion