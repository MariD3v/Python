'''
Sirven para acceder a otros ficheros
'''
import modulo #Con 'Import' llamamos al modulo del que queramos sacar informacion
modulo.suma(3, 4) #Poniendo el nombre del modulo y .accedemos a la función que queramos.

from modulo_2 import PrintTexto #Con 'from' llamamos en especifico a una función de un modulo.
PrintTexto('Hola Mari') #Como hemos llamado en especifico a una funcion, no hce falta poner modulo_2.

'''
Dentro del sistema tenemos distintos módulos 
ya instalados. Podemos usarlos para distintas cosas.
'''
import math #Accedemos al fichero math del sistema
print(math.pi) #Que nos puede dar el valor pi

from math import pow as potencias #Renombramos la función a nuestro gusto.
print(potencias(2, 8))#Potencia, 2 elevado a 8
