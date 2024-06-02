'''
Son funciones, dentro de funciones.
'''
def mas_1(valor):
    return valor + 1

def suma(valor_1, valor_2):
    return mas_1 (valor_1 + valor_2)

print(suma(1, 2))

#Closures

def mas_10(valor__1): #Definimos una funcion dentro de una funcion
    def add(valor__2):
        return valor__2 + 10 + valor__1
    return add

print(mas_10(2)(4)) #El valor 2, corresponde a valor__1 y el 4, a valor__2

#Funciones de orden superior prediseñadas
#Map
'''
Map, se usa con datos iterables, una lista por ejemplo.
Recorre todos los valores para ejecutar una funcion sobre cada valor de una lista.
'''
numeros = [2, 3, 4, 23]
def multiplicar_2(numero):
    return numero * 2

print(list(map(multiplicar_2, numeros)))

#Filter
'''
Filter, se usa con datos iterables, una lista por ejemplo.
Recorre todos los valores y filtra los datos que queramos de cada valor de la lista.
Filter, nos pide que definamos una funcion de True or False,
para saber que tiene que filtrar.
Solamente muestra los True
'''
def filtro_mayor_que_10(numero):
    if numero > 10:
        return True
    return False

print(list(filter(filtro_mayor_que_10, numeros)))

#Reduce
'''
Reduce, se usa con datos iterables, una lista por ejemplo.
Ejecuta una funcion con cada valor de la lista. suma, resta, multiplicacion...
'''
from functools import reduce #Hay que importarlo para usarlo.

print(reduce((lambda valor_1, valor_2: valor_1 + valor_2), numeros)) #Podemos usar una lambda o un funcion.
