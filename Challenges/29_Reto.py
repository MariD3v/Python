'''
ORDENA LA LISTA
Crea una función que ordene y retorne una matriz de números.
- La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
  adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor o de mayor a menor.
- No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
'''

def orden(Orden, matriz):
  if Orden == 'Asc':
    nueva_matriz = []
    for x in range(0, 1000):
      if x in matriz:
        nueva_matriz.append(x)
    return nueva_matriz
  elif Orden == 'Desc':
    nueva_matriz_reves = []
    for x in range(1000, 0, -1):
      if x in matriz:
        nueva_matriz_reves.append(x)
    return nueva_matriz_reves
  else:
    return('Introduce un orden válido')

print(orden('Asc', [23, 5, 45, 12, 1, 24, 55, 7]))
print(orden('Desc', [23, 5, 45, 12, 1, 24, 55, 7]))