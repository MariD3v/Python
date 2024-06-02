'''
Es un conjunto de ejecuciones, almacenadas en una función.
'''
def funcion_1 ():
    print('Esto es una funcion')
funcion_1()

def funcion_sumar (valor_1, valor_2): #Definimos una función
    print(valor_1 + valor_2)
funcion_sumar(1, 3) #La ejecutamos
funcion_sumar(5, 3)
funcion_sumar(1867, 367)

def funcion_retorno (valor_1, valor_2):
    return valor_1 + valor_2 #devuelve un valor ya calculado anteriormente.
valor_anterior = funcion_retorno(0, 4)
print(valor_anterior)

def nombre (nombre, apellidos):
    print(f'{nombre} {apellidos}')
nombre('Mari', 'Salar')  #Es lo mismo que lo de abajo
nombre(nombre = 'Mari', apellidos = 'Salar')

def funcion_por_defecto (nombre, apellidos, nick = 'Sin alias'):
    print(f'{nombre} {apellidos} {nick}')
funcion_por_defecto ('Mari', 'Salar') #Al no poner un 3ºelemento, se aplica por defecto el nick establecido
funcion_por_defecto ('Mari', 'Salar', 'Little')

def funcion_varios_datos (*textos): #Poniendo el asterisco, podemos meter el nº de parámetros que queramos
    for texto in textos: #El for, lo utilizamos para que la lista salga hacia abajo sin ()
        print(texto)
funcion_varios_datos ('Hola', 'Mari', 'Como estas')

def funcion_mayus (*textos):
    for texto in textos:
        print(texto.upper()) #Podemos añadir las terminaciones que queramos
funcion_mayus ('Hola', 'Mari', 'Como estas')

#Lambdas
'''
Son funciones sin nombre
'''
suma = lambda valor_1, valor_2: valor_1 + valor_2
print(suma(2, 3))

