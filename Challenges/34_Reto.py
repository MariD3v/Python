'''
LOS NÚMEROS PERDIDOS
Enunciado: Dado un array de enteros ordenado y sin repetidos, 
crea una función que calcule y retorne todos los que faltan entre el mayor y el menor.
- Lanza un error si el array de entrada no es correcto.
'''

def perdidos(lista):
    ordenados = []
    for x in range (1, 10000):
        if x in lista:
            ordenados.append(x)
    if ordenados != lista:
        return('Lista no ordenada')
    else:
        n_perdidos = []
        numero_de_elementos = len(lista) -1
        ultimo_numero = lista[numero_de_elementos]
        primer_numero = lista[0]
        for x in range(primer_numero, ultimo_numero):
            if x not in lista:
                n_perdidos.append(x)
        return n_perdidos

lista = [3, 4, 6, 7, 8, 10, 13, 20, 22]
print(perdidos(lista))
lista = [3, 4, 6, 7, 8, 1, 10, 13, 20, 22]
print(perdidos(lista))

