'''
TRUCO O TRATO
Este es un reto especial por Halloween.
Deberemos crear un programa al que le indiquemos si queremos realizar "Truco
o Trato" y un listado (array) de personas con las siguientes propiedades:
- Nombre de la niña o niño
- Edad
- Altura en centímetros

Si las personas han pedido truco, el programa retornará sustos (aleatorios)
siguiendo estos criterios:
- Un susto por cada 2 letras del nombre por persona
- Dos sustos por cada edad que sea un número par
- Tres sustos por cada 100 cm de altura entre todas las personas
- Sustos: 🎃 👻 💀 🕷 🕸 🦇

Si las personas han pedido trato, el programa retornará dulces (aleatorios)
siguiendo estos criterios:
- Un dulce por cada letra de nombre
- Un dulce por cada 5 años cumplidos hasta un máximo de 30 años por persona
- Dos dulces por cada 60 cm de altura hasta un máximo de 180 cm por persona
- Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩
'''
import math
import random

def truco_trato(tot, niño):
    if tot == 'Truco': 
        sustos = ['🎃', '👻', '💀', '🕷', '🕸', '🦇']
        n_sustos = 0
        suma_alturas = 0
        for x in range(0, len(niño)):
            suma_alturas += niño[x][2] 
            n_sustos += math.trunc(len(niño[x][0])/2)
            if niño[x][1] % 2 == 0:
                n_sustos += 2
        multiplicador_altura = math.trunc(suma_alturas / 100)
        if multiplicador_altura > 0:
            n_sustos += multiplicador_altura*3
        sustos_azar = random.choices(sustos, k=n_sustos)
        print(sustos_azar)

    elif tot == 'Trato':
        dulces = ['🍰', '🍬', '🍡', '🍭', '🍪', '🍫', '🧁', '🍩']
        n_dulces = 0
        for x in range(0, len(niño)):
            n_dulces += len(niño[x][0])
            if niño[x][1] < 30:
                n_dulces += math.trunc(niño[x][1]/5)
            if niño[x][2] < 180:
                n_dulces += math.trunc(niño[x][2]/60)*2
        dulces_azar = random.choices(dulces, k=n_dulces)
        print(dulces_azar)

niños = [['Mari', 23, 170],
         ['Miguel', 25, 190]]
truco_trato('Truco', niños)
truco_trato('Trato', niños)