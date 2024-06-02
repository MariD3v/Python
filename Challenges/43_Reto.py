'''
CONTENEDOR DE AGUA
Dado un array de números enteros positivos, donde cada uno representa unidades 
de bloques apilados, debemos calcular cuantas unidades de agua quedarán 
atrapadas entre ellos.
- Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].

          ⏹
          ⏹
   ⏹💧 💧⏹
   ⏹💧⏹⏹💧⏹
   ⏹💧⏹⏹💧⏹
   ⏹💧⏹⏹⏹⏹

Representando bloque con ⏹︎ y agua con 💧, quedarán atrapadas 7 unidades de agua.
Suponemos que existe un suelo impermeable en la parte inferior que retiene el agua.
'''
def contenedor(array):
    izquierda = 0
    derecha = len(array) - 1
    izquierda_max = 0
    derecha_max = 0
    agua = 0

    while izquierda < derecha: 
        if array[izquierda] < array[derecha]:
            if array[izquierda] > izquierda_max:
                izquierda_max = array[izquierda]
            else:
                agua += izquierda_max - array[izquierda]
            izquierda += 1
        else:
            if array[derecha] > derecha_max:
                derecha_max = array[derecha]
            else:
                agua += derecha_max - array[derecha]
            derecha -= 1

    return agua

array = [4, 0, 3, 6, 1, 3]
print(contenedor(array)) 
array = [2, 5, 7, 6, 4, 2, 7, 2, 4]
print(contenedor(array))