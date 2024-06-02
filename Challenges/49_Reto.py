'''
EL PARTIDO DE TENIS
Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
gane cada punto del juego.
- Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
- Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
  15 - Love
  30 - Love
  30 - 15
  30 - 30
  40 - 30
  Deuce
  Ventaja P1
  Ha ganado el P1
- Si quieres, puedes controlar errores en la entrada de datos.   
- Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
'''
def tenis(secuencia):
    p1 = 0 
    p2 = 0
    for x in range(len(secuencia)):
        if secuencia[x] == 'P1':
            p1 += 1
        elif secuencia[x] == 'P2':
            p2 += 1

        puntos = f'{p1} - {p2}'

        if p1 >= 3 and p2 >= 3:
            if p1 == p2:
                puntos = 'Deuce'
            elif p1 > p2:
                puntos = 'Ventaja P1'
            else:
                puntos = 'Ventaja P2'

        if p1 > 3 and p1 - p2 >= 2:
            puntos = 'Gana P1'
        elif p2 > 3 and p2 - p1 >= 2:
            puntos = 'Gana P2'

        print(puntos)

partido_1 = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']
tenis(partido_1)
partido_2 = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P2', 'P1']
tenis(partido_2)
partido_3 = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P2', 'P2']
tenis(partido_3)
partido_4 = ['P1', 'P2', 'P1', 'P2', 'P2', 'P2']
tenis(partido_4)

