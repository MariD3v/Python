'''
BINARIO A DECIMAL
Enunciado: Crea un programa se encargue de transformar un número binario a decimal 
sin utilizar funciones propias del lenguaje que  lo hagan directamente.
'''
def binario(n_binario):
    n_binario = list(str(n_binario))
    decimal = 0
    n_de_caracteres = len(n_binario)
    for x in n_binario:
        x = int(x)
        decimal += x*(2**(n_de_caracteres- 1))
        n_de_caracteres = n_de_caracteres - 1
    return decimal
print(binario(10101))
print(binario(101))
print(binario(101011))
print(binario(101101))