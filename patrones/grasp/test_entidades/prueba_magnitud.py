from patrones.grasp.entidades.magnitud import *

mi_magnitud = Magnitud("Hematies", "mm3")
valor1 = ValorReferencia("Valor de Referencia Inferior", 4400000)
valor2 = ValorReferencia("Valor de Referencia Superior", 5900000)
mi_magnitud.agregar_valor_referencia(valor1)
mi_magnitud.agregar_valor_referencia(valor2)

print (mi_magnitud)
for valor in mi_magnitud.valores_referencia:
    print(str(valor) + " " + str(mi_magnitud.unidad_de_medida))
