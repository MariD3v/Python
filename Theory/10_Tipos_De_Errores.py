#SyntaxError
print 'Hola' #Faltan ()

#NameError
print(variable) #Falta definir la variable

#IndexError
lista = ['Python', 'Swift', 'Kotlin']
print(lista[3]) #No hay elemento 0

#ModuleNotFoundError
import maths #No existe maths

#AttributeError
print('hola'.COUNT) #Es sin mayus

#KeyError
dict_1 = {'Nombre':'Mari', 'Edad':23, 'Altura':1.70}
print(dict_1['Eda']) #No existe Eda

#TypeError
print(lista['Python']) #Debe accederse en una lista con numeros

#ImportError
from math import PI #Es sin mayus

#ValueError
mi_int = int('10 años') #No se puede hacer int de años

#ZeroDivisionError
print(4/0) #No se puede dividir entre 0