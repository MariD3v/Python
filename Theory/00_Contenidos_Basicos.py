#Esto es un comentario
"""
Esto es un comentario 
en varias
lineas
"""
#Print (Muestra un dato, una variable, una lista, una tupla...)
print("Hola Mari")
print('Hola Mari')

#Tipos de datos
print(type("Soy un dato str")) #Tipo "Str"
print(type(5)) #Tipo "int"
print(type(1.5)) #Tipo "float"
print(type(True)) #Tipo "bool"
print(type(1+3j)) #Tipo "complex"

###Variables###
"""
Las variables en Python deben ir en minúsculas siempre,
separando las palabras con _
"""

my_string_variable = "My String variable"
print(my_string_variable)

menú = "costillas"
print(menú)

my_int_variable = 5
print(my_int_variable)

cantidad = 10
print(cantidad)

my_bool_variable = False
print(my_bool_variable)

casado = True
print(casado)

#Concatenación de variables
print(my_string_variable, my_int_variable, my_bool_variable) 
print("Este es el valor de", cantidad)

#Variables en una sola linea
name, surname, age = "Mari", "Salar", 23
print("Me llamo", name, surname, "y mi edad es", age,"años" )

#Variables en varias lineas
name2 = "Mari \nSalar"
print(name2)

#Variables con tabulador
name3= "\tMari"
print(name3)

#Formateo
 
name4, surname4, age4 = "Mari", 'Salar', 23
print('Me llamo {} {} y mi edad es {}'.format(name4, surname4, age4))
print('Me llamo %s %s y mi edad es %d' %(name4, surname4, age4)) # %s para str %d para int
print(f'Me llamo {name4} {surname4} y mi edad es {age4}') # la f sirve para formatear 

#Juego de caracteres
palabra = 'MariTierra'
a, b, c, d, e, f, g, h, i, j = palabra
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
primeras_3_letras = palabra[0:3]
print(primeras_3_letras)
desde_la_letra_3_al_final = palabra[3:]
print(desde_la_letra_3_al_final)
letra_3_por_el_final = palabra[-3]
print(letra_3_por_el_final)
palabra_alreves = palabra[::-1]
print(palabra_alreves)

#Funciones
print(palabra.capitalize()) #Pone el Mayus la primera letra
print(palabra.count('t')) #Cuenta cuantas letras 't' hay
print(palabra.upper()) #Todo en mayus
print(palabra.isnumeric()) #Para saber si es numerico
print(palabra.lower()) #Todas minus
print(palabra.isupper())#Para saber si hay alguna mayus
