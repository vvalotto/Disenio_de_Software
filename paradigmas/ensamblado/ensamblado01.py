import dis


def saludar(persona):
    print('Hola ' + persona)


def suma(x, y):
    print(x + y)


def lazo():
    for i in range(0, 10):
        print(i)


def eleccion(opcion):
    if opcion is None:
        print('Nada')
    else:
        print(opcion)

def umbral():
    for x in range(0, 5):
        if x > 4:
            y = x + 5
            print(y)


print('Ejemplo 1: SALUDAR')
dis.dis(saludar)
print()

print('Ejemplo 1: SUMA')
dis.dis(suma)
print()

print('Ejemplo 1: LAZO')
dis.dis(lazo)
print()

print('Ejemplo 1: ELECCION')
dis.dis(eleccion)
print()

print('Ejemplo 1: UMBRAL')
dis.dis(umbral)
print()
