'''
¿DÓNDE ESTÁ EL ROBOT?
Calcula dónde estará un robot (sus coordenadas finales) que se encuentra en una cuadrícula 
representada por los ejes "x" e "y".
- El robot comienza en la coordenada (0, 0).
- Para idicarle que se mueva, le enviamos un array formado por enteros (positivos o negativos) 
que indican la secuencia de pasos a dar en circulos.
- Por ejemplo: [10, 5, -2] indica que primero se mueve 10 pasos en el eje y, se detiene,
  luego 5 en el eje x, se detiene, y finalmente 2 en el eje y. 
  El resultado en este caso sería (x: -5, y: 12)
- Si el número de pasos es negativo, se desplazaría en sentido contrario al que está mirando.
- Los primeros pasos los hace en el eje "y". Interpretamos que está mirando hacia la parte positiva 
del eje "y".
- El robot tiene un fallo en su programación: cada vez que finaliza una secuencia de 1 vuelta
gira 90 grados en el sentido contrario a las agujas del reloj.
'''
def robot(movimientos):
    coordenadas_finales = [0, 0]
    direccion = 0  
    #0: mirando hacia arriba (eje y positivo), 1: mirando hacia la izquierda, 2: mirando hacia abajo, 3: mirando hacia la derecha

    for movimiento in movimientos:
        if direccion == 0:
            coordenadas_finales[1] += movimiento
        elif direccion == 1:
            coordenadas_finales[0] -= movimiento
        elif direccion == 2:
            coordenadas_finales[1] -= movimiento
        elif direccion == 3:
            coordenadas_finales[0] += movimiento

        direccion = (direccion - 1) % 4  # Girar 90 grados en sentido contrario a las agujas del reloj

    return {'x': coordenadas_finales[0], 'y': coordenadas_finales[1]}

print(robot([2, -1, 12, -10]))