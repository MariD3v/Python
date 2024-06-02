'''
MARCO DE PALABRAS
Crea una función que reciba un texto y muestre cada palabra en una línea,
formando un marco rectangular de asteriscos.
- ¿Qué te parece el reto? Se vería así:
**********
* ¿Qué   *
* te     *
* parece *
* el     *
* reto?  *
**********
'''
def marco(texto):
    texto_listado = texto.split()
    palabras_maslarga = ''
    for x in texto_listado:
        if len(x) > len (palabras_maslarga):
            palabras_maslarga = x
    texto_marco = '*'*(len(palabras_maslarga)+ 4)+ '\n'
    for x in range(0, len(texto_listado)):
        texto_marco += '* ' + texto_listado[x] + (' '*(len(palabras_maslarga)+ 1 - len(texto_listado[x]))) + '*\n'
    texto_marco += '*'*(len(palabras_maslarga)+ 4)   
    print(texto_marco)
    

marco('Hola como estas')
marco('Me llamo Mari, mi perrito se llama Urus')