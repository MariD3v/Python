'''
EL GENERADOR DE CONTRASEÑAS
Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
Podrás configurar generar contraseñas con los siguientes parámetros:
- Longitud: Entre 8 y 16.
- Con o sin letras mayúsculas.
- Con o sin números.
- Con o sin símbolos.
(Pudiendo combinar todos estos parámetros entre ellos)
'''
import random
import string
letras_mayusculas = string.ascii_uppercase
letras_minusculas = string.ascii_lowercase
numeros = string.digits
simbolos = string.punctuation
conjunto = simbolos + numeros + letras_mayusculas + letras_minusculas

def contraseña():
    numero_entre8y16 = random.randint(8, 16)
    password = ''
    for x in range(numero_entre8y16):
        password += random.choice(conjunto)
    return password

print(contraseña())