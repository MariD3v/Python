'''
BATALLA POKÉMON
Enunciado: Crea un programa que calcule el daño de un ataque durante una batalla Pokémon.
- La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
- Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
- Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico (buscar su efectividad)
- El programa recibe los siguientes parámetros:
- Tipo del Pokémon atacante.
- Tipo del Pokémon defensor.
- Ataque: Entre 1 y 100.
- Defensa: Entre 1 y 100.
Fuego - Planta = x2
Eléctrico - Agua = x2
Planta - Agua = x2
Agua - Fuego = x2
Planta - Eléctrico = x1
Agua - Eléctrico = x1
Eléctrico - Fuego = x1
Fuego - Eléctrico = x1
Planta - Fuego = x0.5
Agua - Planta = x0.5
Eléctrico - Planta = x0.5
Fuego - Agua = x0.5
Fuego - Fuego = x0.5
Agua - Agua = x0.5
Planta - Planta= x0.5
Eléctrico - Eléctrico = x0.5
'''
def pokemon(atacante, ataque, defensor, defensa):
    if atacante == 'Fuego' and defensor == 'Planta' or atacante == 'Eléctrico' and defensor == 'Agua' or atacante == 'Planta' and defensor == 'Agua' or atacante == 'Agua' and defensor == 'Fuego':
        efectividad = 2
    elif atacante == 'Planta' and defensor == 'Eléctrico' or atacante == 'Agua' and defensor == 'Eléctrico' or atacante == 'Fuego' and defensor == 'Eléctrico' or atacante == 'Eléctrico' and defensor == 'Fuego':
        efectividad = 1
    else:
        efectividad = 0.5
    daño = 50 * (ataque/defensa) * efectividad
    return daño

print(pokemon('Planta',68, 'Fuego', 70))
print(pokemon('Agua', 89, 'Eléctrico', 89))
print(pokemon('Agua', 46, 'Agua', 65))
print(pokemon('Eléctrico', 89, 'Fuego', 70))
print(pokemon('Agua', 60, 'Planta', 100))