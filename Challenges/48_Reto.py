'''
EL "LENGUAJE HACKER"
Escribe un programa que reciba un texto y transforme lenguaje natural a "lenguaje hacker" 
(conocido realmente como "leet" o "1337"). Este lenguaje se caracteriza por sustituir caracteres alfanuméricos.
- Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) con el alfabeto y 
los números en "leet". (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 '''
map_leet = {
'A': '4',
'B': 'I3',
'C': '[',
'D': ')',
'E': '3',
'F': '|=',
'G': '&',
'H': '#',
'I': '1',
'J': ',_|',
'K': '>|',
'L': '1',
'M': '[V]',
'N': '^/',
'O': '0',
'P': '|*',
'Q': '(_,)',
'R': 'I2',
'S': '5',
'T': '7',
'U': '(_)',
'V': '\/',
'W': '\/\/',
'X': '><',
'Y': 'J',
'Z': '2',
}

def hacker(texto):
    texto = texto.upper()
    traduccion = ''
    for x in texto:
        if x in map_leet:
            traduccion += map_leet[x]
        elif x == ' ':
            traduccion += ' '
    return traduccion

print(hacker('Hola me llamo Mari'))