'''
PRIMO, FIBONACCI Y PAR
Escribe un programa que, dado un número, compruebe y muestre si es primo,
fibonacci y par.
Ejemplos:
- Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
- Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
'''
def primo(numero):
    if numero < 2:
        return False
    for x in range(2, numero):
        if numero % x == 0:
            return False
    return True

def fibonacci(numero):
    anterior = 0
    siguiente = 1

    fb_list = []
    for x in range(20):
        fb_list.append(anterior)
        fibonacci = anterior + siguiente
        anterior = siguiente
        siguiente = fibonacci
    
    if numero in fb_list:
        return True
    else:
        return False
    
def par_1(numero):
    if numero == 0:
        return True
    elif numero % 2 == 0:
        return True
    else:
        return False

def todo(numero):
    
    if primo(numero) == True:
        pr = ' es primo, '
    else:
        pr = ' no es primo, '

    if fibonacci(numero) == True:
        fb = 'es fibonacci, '
    else:
        fb = 'no es fibonacci, '

    if par_1(numero) == True:
        par = 'es par.'
    else:
        par = 'no es par.'
    
    texto = str(numero) + pr + fb + par

    return texto

print(todo(1))
print(todo(2))
print(todo(9))
print(todo(3))

