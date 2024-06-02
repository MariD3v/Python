'''
TRIÁNGULO DE PASCAL
Crea una función que sea capaz de dibujar el "Triángulo de Pascal" 
indicándole únicamente el tamaño del lado.
 - Aquí puedes ver rápidamente cómo se calcula el triángulo:
https://commons.wikimedia.org/wiki/File:PascaltrianguloAnimated2.gif
'''
def triangulo_de_pascal(altura):
    triangulo = []
    for y in range(altura):
        fila = [1]
        for x in range(1, y):          
            elemento_intermedio = triangulo[y - 1][x - 1] + triangulo[y - 1][x]
            fila.append(elemento_intermedio)
        if y > 0:
            fila.append(1)
        triangulo.append(fila)

    for j in triangulo:
        print(j)


triangulo_de_pascal(5)