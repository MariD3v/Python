'''
EL GENERADOR PSEUDOALEATORIO
Crea un generador de números pseudoaleatorios entre 0 y 100.
- No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
Es más complicado de lo que parece...
'''
from datetime import datetime

def generador():
    now = datetime.now()
    timestamp = now.timestamp()
    timestamp_count = len(str(timestamp))
    timestamp_list  = [caracter for caracter in str(timestamp)]
    numero = ''
    for x in range(timestamp_count - 1, timestamp_count - 3, -1):
        numero += timestamp_list[x]
    return numero

print(generador())