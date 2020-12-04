

def filtrar_caracteres_alfabeticos(texto):

    caracteres_descartables = [',', '.', ':', ';', '-', '_']
    texto_filtrado = ''
    for caracter in texto:
        if caracter not in caracteres_descartables:
            texto_filtrado += caracter

    return texto_filtrado


def depurar_texto(texto):

    texto_con_palabras = filtrar_caracteres_alfabeticos(texto)
    texto_con_palabras_en_minusculas = texto_con_palabras.lower()

    return texto_con_palabras_en_minusculas


def obtener_palabras(texto):
    texto_depurado = depurar_texto(texto)
    lista_de_palabras = texto_depurado.split()

    return lista_de_palabras


def contar_palabras(texto):
    return len(obtener_palabras(texto))


def obtener_palabras_iniciadas_con(texto, letra):
    lista_de_palabras = []
    for palabra in obtener_palabras(texto):
        if palabra[0] == letra:
            lista_de_palabras.append(palabra)

    return lista_de_palabras


def contar_palabras_iniciadas_con(texto, letra):
    return len(obtener_palabras_iniciadas_con(texto, letra))
