'''
Una lista, es una forma de agrupar datos 
de forma ordenada, con repetidos y mutable.
'''
lista = ['Mari', 23, 1.70]
lista_2 = list()

print(lista)
print(len(lista)) #nº de datos
print(type(lista)) #De tipo Lista
print(lista[0]) #Dato que ocupa la posición 0 en la lista
print(lista[-1]) #Dato que ocupa la posición 1 en la lista empezando por el final
print(lista.count('Mari')) #Cuenta cuantos 'Mari' hay en la lista
print(lista.index(23)) #Nos dice en que posición se encuentra '23'

#Mutar las listas
lista.append('Morena') #Añade otro elemento a la lista
lista.insert(1, 'Mujer') #Elige en que posición meter un elemento
lista.remove('Morena') #Elimina un elemento de la lista
nueva_lista = lista.copy() #Copia una lista creando otra
lista.pop() #Quita el último elemento de la lista
lista.pop(2) #Quita el segundo elemento de la lista
lista.clear() #Elimina todos los elementos de la lista

lista_numerica = [12, 34, 54, 2, 34]
lista_numerica.sort() #Ordena los elementos

#Comprimir listas

rango = range(8) #Crear una lista de rango 8
print(list(rango))

lista_rango = [x for x in range(8)]#Otra opción de una lista de rango 8
lista_rango1 = [x + 1 for x in range(8)]
lista_de2en2 = [x * 2 for x in range(8)] #Lista de 2 en 2
print(lista_rango)
print(lista_rango1)
print(lista_de2en2)

'''
Una tupla, es una forma de agrupar datos 
de forma ordenada, con repetidos pero inmutable.
'''
tupla = ('Mari', 23, 1.70)
tupla2 = tuple()

print(tupla)
print(len(tupla)) #nº de datos
print(type(tupla)) #De tipo Tupla
print(tupla[0]) #Dato que ocupa la posición 0 en la tupla
print(tupla[-1]) #Dato que ocupa la posición 1 en la tupla empezando por el final
print(tupla.count('Mari')) #Cuenta cuantos 'Mari' hay en la tupla
print(tupla.index(23)) #Nos dice en que posición se encuentra '23'

#Mutar las tuplas
'''
No se pueden mutar, esa es la principal diferencia con las listas.
'''
