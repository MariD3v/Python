#PIP
'''
Encuentra, instala y publica modulos/paquetes de Python.
'''

#Instalarlo

  #Comprobamos que esta instalado en la terminal poniendo 'pip --version'

#Instalar paquetes

  #Ponemos en la terminal 'pip install moduloquequeremos' y reiniciamos el programa y lo importamos:

import numpy #Nos da operaciones mas complejas con numeros

#Acceder a paquetes creados por nosotros

from mypackage import aritmetica

print(aritmetica.funcion_sumar(1, 3))