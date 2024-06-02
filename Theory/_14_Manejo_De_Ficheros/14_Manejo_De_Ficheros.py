#Utilizamos 'r' para lectura, 'w' para escritura y 'a' para añadir al final del archivo.
'''
'w+': Se utiliza para crear archivos y poder leerlos y escribir. 
No sirve para archivos existentes pues los borra

'r+': Solo sirve para archivos existentes. Si el archivo no existe, se produce un error.
 Puedes utilizar tanto operaciones de escritura como de lectura en el archivo abierto. 
'''
#.txt 

archivo = open('Teoria\_14_Manejo_De_Ficheros\Fichero.txt', 'r+') #Abrimos el archivo en modo lectura y escritura
print(archivo.read(10)) #Se leen los 20 primeros caracteres
print(archivo.readline()) #Se lee lo que queda de la primera linea
print(archivo.readline()) #Lee una nueva linea entera
print(archivo.readlines()) #Lee las linea restantes
archivo.write('\nMi perro se llama Urus') #escribimos una linea nueva de texto
archivo.close() #Cerrar el archivo. Siempre debe cerrarse para guardar el proceso

#.json
'''
Un archivo json es un archivo de tipo clave:valor. Parecido a un diccionario.
'''
import json #Para poder trabajar ocn archivos .json

archivo_json = open('Teoria\_14_Manejo_De_Ficheros\Archivo.json', 'w+') #Creamos un archivo .json

test_json = {
    'Nombre':'Mari',
    'Apellidos':'Salar',
    'Color':['Rosa', 'Azul', 'Amarillo'],
    'Edad':23} 

json.dump(test_json, archivo_json, indent = 2) #Para incorporar datos en .json usamos .dump(lo queremos incorporar, el fichero donde lo incorporamos, y la identacion que queremos)
archivo_json.close()
with open('Teoria\_14_Manejo_De_Ficheros\Archivo.json') as archivo_json2:  #Para leer el archivo json
    for linea in archivo_json2.readlines():
        print(linea)

json_dict = json.load(open('Teoria\_14_Manejo_De_Ficheros\Archivo.json')) #Para recuperar el diccionario
print(json_dict)

#.csv 
'''
Es una especie de excel
'''
import csv

#.xlsx

'''import xlrd, debe instalarse el modulo para usarse'''

#.xml

import xml