'''
HETEROGRAMA, ISOGRAMA Y PANGRAMA
Crea 3 funciones, cada una encargada de detectar si una cadena de texto es un heterograma, 
un isograma o un pangrama.
- Debes buscar la definición de cada uno de estos términos.
'''
def heterograma(texto):
    lista_palabras = texto.lower().split()
    for x in range(len(lista_palabras)):
        acumulacion = ''
        for y in lista_palabras[x]:
            if y in acumulacion:
                return False
            acumulacion += y
    return True

print(heterograma('Mi nombre es Mari'))
print(heterograma('Me llamo Maria, tengo 23 años y vivo en Murcia'))

def isograma(texto):
    if ' ' in texto:
        lista_palabras = texto.lower().split()
        for x in range(len(lista_palabras)):
            for y in lista_palabras[x]:
                if y*2 in lista_palabras[x]:
                    return True    
    else:
        texto = texto.lower()
        acumulacion = []
        for x in texto:
            if x in acumulacion:
                acumulacion.remove(x)
            else:
                acumulacion += x
        if len(acumulacion) == 0:
                return True
    return False

print(isograma('mama'))
print(isograma('hola como estas'))

def pangrama(texto):
    texto = texto.lower()
    
    acumulacion = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    for x in texto:
        if x in acumulacion:
            acumulacion.remove(x)
        else:
            continue
    if len(acumulacion) == 0:
        return True
    return False

print(pangrama('abcdefghijklmnñopqrstuvwxyz'))
print(pangrama('Un jugoso zumo de piña y kiwi bien frío es exquisito y no lleva alcohol'))
print(pangrama('hola, esto no es un pangrama'))
print(pangrama('Esto tampoco es un pangrama'))