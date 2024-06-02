'''
CONVERSOR DE TEMPERATURA
Crea una función que transforme grados Celsius en Fahrenheit y viceversa.
- Para que un dato de entrada sea correcto debe poseer un símbolo "°" y su unidad ("C" o "F").
- En caso contrario retornará un error.
'''
import re
def temperatura(grados):
    if re.search('°C', grados):
        grados = grados.replace('°C', '')
        grados_transformados = (int(grados)*9/5) + 32
        print(grados_transformados)
    elif re.search('°F', grados):
        grados = grados.replace('°F', '')
        grados_transformados = (int(grados)-32)*5/9
        print(grados_transformados)
    else:
        print('Introduce el dato seguido de °F o °C')

temperatura('20°F')
temperatura('24°C')
temperatura('2°F')
