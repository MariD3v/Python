'''
Un set, es una forma de agrupar datos 
de forma desordenada, sin repetidos y mutable.
'''
set_1 = {'Mari', 23, 1.70}
set_2 = set()

print(set_1)
print(len(set_1)) #Nº de datos
print(type(set_1)) #De tipo Set
#print(set_1[0]) #ERROR No puedes buscar un elemento en tal posición si no hay orden.
#print(set_[-1]) #ERROR No puedes buscar un elemento en tal posición si no hay orden.
#print(set_1.count('Mari')) #ERROR No puedes buscar cuantos elementos hay si solo puede haber 1 de cada.

#Mutar un set
set_1.add('Morena') #Añade un elemento de forma desordenada.
set_1.add('Morena') #No admite repetir 2 elementos.
set_1.remove('Morena') #Elimina un elemento.
set_1.clear() #Elimina todos los elementos del set

set_1 = {'Mari', 23, 1.70}
set_3 = {'Miguel', 25, 1.90}

set_1_y_3 = set_1.union(set_3) #Une 2 sets de forma desordenada
print(set_1_y_3)
print(set_1_y_3.difference(set_3)) #Busca las diferencias en los elementos de 2 sets

'''
Un diccionario, es una forma de agrupar datos
de tipo clave:valor, de forma ordenada y mutable.
'''
dict_1 = {'Nombre':'Mari', 'Edad':23, 'Altura':1.70}
dict_2 = dict()
#Otra forma de mostrar diccionarios
dict_3 = {
    'Nombre':'Mari',
    'Apellidos':'Salar',
    'Color':'Rosa',
    'Edad':25
} 

print(dict_1)
print(len(dict_1)) #Nº de claves
print(type(dict_1)) #De tipo Dict
print(dict_1['Nombre']) #Para acceder al valor de una clave en concreto.
print(dict_1.items()) #Todos los clave:valor
print(dict_1.keys()) #Todas las claves
print(dict_1.values()) #Todos los valores

#Añadir un valor:clave o varios valor:clave
'''
Dentro del diccionario se pueden meter 
tanto un valor, como sets, como listas, 
como tuplas, como otro diccionario.
'''
dict_3['Mascotas'] = ('Urus', 'Melody') #Añadiendo una lista

dict_3['Gustos'] = {'Flores', 'Libros', 'Juegos', 'Perros'} #Añadiendo un set

dict_3['Aficiones'] = ['Comprar', 'Pasear'] #Añadiendo una tupla

dict_3['Novio'] = {      #Añadiendo un diccionario
    'Nombre':'Miguel',
    'Edad':25,
    'Altura':1.90
    }    

print(dict_3)