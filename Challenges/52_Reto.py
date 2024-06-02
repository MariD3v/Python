'''
PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK
Crea un programa que calcule quien gana más partidas al piedra, papel, tijera, lagarto, spock.
- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
- La función recibe un listado que contiene pares, representando cada jugada.
- El par puede contener combinaciones de "🗿" (piedra), "📄" (papel), "✂️" (tijera), "🦎" (lagarto) 
o "🖖" (spock).
- Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
- Debes buscar información sobre cómo se juega con estas 5 posibilidades.
'''
def p_p_t_l_s(entrada):
    player_1 = 0
    player_2 = 0
    for x in range(len(entrada)):
        if entrada[x][0] == '🗿' and entrada[x][1] == '✂️':
            player_1 += 1
        elif entrada[x][0] == '✂️' and entrada[x][1] == '🗿':
            player_2 += 1        
        if entrada[x][0] == '🗿' and entrada[x][1] == '📄':
            player_2 += 1
        if entrada[x][0] == '📄' and entrada[x][1] == '🗿':
            player_1 += 1
        if entrada[x][0] == '🗿' and entrada[x][1] == '🦎':
            player_1 += 1
        if entrada[x][0] == '🦎' and entrada[x][1] == '🗿':
            player_2 += 1
        if entrada[x][0] == '🗿' and entrada[x][1] == '🖖':
            player_2 += 1
        if entrada[x][0] == '🖖' and entrada[x][1] == '🗿':
            player_1 += 1
        if entrada[x][0] == '✂️' and entrada[x][1] == '📄':
            player_1 += 1
        if entrada[x][0] == '📄' and entrada[x][1] == '✂️':
            player_2 += 1
        if entrada[x][0] == '🦎' and entrada[x][1] == '📄':
            player_1 += 1
        if entrada[x][0] == '📄' and entrada[x][1] == '🦎':
            player_2 += 1        
        if entrada[x][0] == '🖖' and entrada[x][1] == '📄':
            player_2 += 1
        if entrada[x][0] == '📄' and entrada[x][1] == '🖖':
            player_1 += 1
        if entrada[x][0] == '✂️' and entrada[x][1] == '🦎':
            player_1 += 1
        if entrada[x][0] == '🦎' and entrada[x][1] == '✂️':
            player_2 += 1
        if entrada[x][0] == '✂️' and entrada[x][1] == '🖖':
            player_2 += 1
        if entrada[x][0] == '🖖' and entrada[x][1] == '✂️':
            player_1 += 1
        if entrada[x][0] == '🦎' and entrada[x][1] == '🖖':
            player_1 += 1
        if entrada[x][0] == '🖖' and entrada[x][1] == '🦎':
            player_2 += 1
    if player_1 > player_2:
        ganador = 'Player_1'
    elif player_2 > player_1:
        ganador = 'Player_2'
    else:
        ganador = 'Empate'

    return ganador


partida_1 = [("🗿","✂️"), ("🗿","🦎"), ("📄","🦎"),("🗿","✂️"), ("🗿","🖖"), ("📄","✂️")]
print(p_p_t_l_s(partida_1))