'''
EL SEGUNDO
Dado un listado de números, encuentra el SEGUNDO más grande.
'''
def segundo(lista):
    lista_ordenada = []
    for x in range(10000, 0, -1):
        if x in lista:
            lista_ordenada.append(x)

    return lista_ordenada[1]

matriz = [12, 43, 4, 23, 56, 432, 245, 20, 3]
print(segundo(matriz))