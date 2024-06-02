'''
Sirven para en una cadena de texto comprobar x cosas.
'''
cadena_texto = 'Esta es la lección numero 15. Lección expresiones regulares' #Trabajaremos sobre esta cadena de texto
import re
#Match
'''
Sirve para encontrar un texto al principio de una cadena
'''
print(re.match('Esta es', cadena_texto, re.I)) #Para encontrar un patron. Si lo encuentra lo retorna y si no retorna 'none'
print(re.match('Esta no es', cadena_texto, re.I)) #Usamos re.I para que ignore si esta en mayus o no.
print((re.match('Esta es', cadena_texto, re.I)).span()) #Te dice la posicion de la frase que buscas

#Search
'''
Sirve para encontrar un texto en cualquier posicion de la cadena
'''
print(re.search('numero', cadena_texto, re.I)) 
print((re.search('numero', cadena_texto, re.I)).span()) #Dice la posición 

#Findall
'''
Nos indica cuantas veces aparece un texto
'''
print(re.findall('lección', cadena_texto, re.I)) 

#Split
'''
Busca un patron con un caracter, y divide la cadena en dos.
'''
print(re.split(',', cadena_texto))

#Sub
'''
Cambia una palabra por otra.
'''
print(re.sub('numero', 'número', cadena_texto))
print(re.sub('[l|L]ección', 'LECCION', cadena_texto)) #Cambia las 2 'leccion'

#Patrones
#https://regex101.com para comprobar patrones
'''
Para escribir expresiones regulares se usa r'LoQueBusca'
'''
patron = r'[Ll]ección'
print(re.findall(patron, cadena_texto))

patron = r'[a-z]'
print(re.findall(patron, cadena_texto)) #Retorna minusculas hay

patron = r'[0-9]'
print(re.findall(patron, cadena_texto)) #Retorna los numeros que hay
print(re.search(patron, cadena_texto)) #Busca los numeros entre 0 y 9 e indica su posicion si hubieran.

patron = r'\d'
print(re.findall(patron, cadena_texto)) #Retorna los caracteres numericos

patron = r'\D'
print(re.findall(patron, cadena_texto)) #Retorna los caracteres no numericos

patron = r'[A-Za-z0-9]'
print(re.findall(patron, cadena_texto)) #Retorna todos los caracteres

patron = r'[l].'
print(re.findall(patron, cadena_texto)) #Retorna la letra 'l' seguida del siguiente caracter

#Expresion regular para email

patron = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$'
email = 'maria@hotmail.com'

print(re.findall(patron, email))
print(re.search(patron, email))
'''
Aquí está el desglose de la expresión regular:

[a-zA-Z0-9_.+-] Esta parte representa el nombre de usuario en la dirección de correo electrónico.
@ coincide con el símbolo "@" literal en la dirección de correo electrónico.
[a-zA-Z0-9-]+ Esta parte representa el dominio del correo electrónico.
\. coincide con un punto (.) literal en la dirección de correo electrónico. 
Como el punto tiene un significado especial en expresiones regulares, 
se le añade una barra invertida \ para que se interprete como un carácter literal.
[a-zA-Z-.]+ Esto representa la extensión del dominio del correo electrónico.
$ indica el final de la cadena, lo que significa que la expresión regular debe coincidir con toda la cadena 
y no permitir ningún carácter adicional después.
'''