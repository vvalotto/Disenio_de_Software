

texto = 'Resistir y persistir. Entender con claridad, actuar con corrección y aceptar lo que fuera'

letra = 'c'
print([ palabra for palabra in texto if palabra[0] != letra])


'''
lista_de_letras = [caracter for caracter in texto if caracter not in ['.', ',']]
oracion = ''.join(lista_de_letras)
print(oracion)


def filtrar_texto(texto, caracter_no_deseado):

    texto_filtrado = ''
    for caracter in texto:
        if caracter is not caracter_no_deseado:
            texto_filtrado += caracter
    return texto_filtrado


print(filtrar_texto(filtrar_texto(texto, '.'), ',').split())

print(list(texto))
'''