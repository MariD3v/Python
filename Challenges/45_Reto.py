'''
VOCAL MÁS COMÚN
Crea un función que reciba un texto y retorne la vocal que más veces se repita.
- Ten cuidado con algunos casos especiales.
- Si no hay vocales podrá devolver vacío.
'''
def vocal(texto):
    texto = texto.lower()
    vocales = ['a','e','i','o','u']
    vocal = ['a','e','i','o','u']
    if any(x in texto for x in vocales) == False:
        return('No hay vocales')
    else:
        if texto.count('a') != 0:
            vocal[0] = texto.count('a')
        if texto.count('e') != 0:
            vocal[1] = texto.count('e')
        if texto.count('i') != 0:
            vocal[2] = texto.count('i')
        if texto.count('o') != 0:
            vocal[3] = texto.count('o')
        if texto.count('u') != 0:
            vocal[4] = texto.count('u')

        for x in range(0, 5):
            if vocal[x] in vocales:
                vocal[x] = 0
        posi_vocal_repetida = vocal.index(max(vocal))
        vocal_repetida = vocales[posi_vocal_repetida]

        if vocal.count(max(vocal)) >= 2:
            return 'Hay empate de vocales más repetidas'
        else:
            return vocal_repetida


print(vocal('Hola me llamo Maria, tengo 23 años'))
print(vocal('El nombre de mi perro es Urus'))
print(vocal('Ui que cuqui'))
print(vocal('Yo no como lomo'))
print(vocal('hola'))
print(vocal('wps'))