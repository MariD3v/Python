'''
AÑOS BISIESTOS
Crea una función que imprima los 30 próximos años bisiestos siguientes a uno dado.
- Utiliza el menor número de líneas para resolver el ejercicio.
'''
def bisiestos(año):
    años_bisiestos = []
    for x in range(0, 5000):
        if x % 4 == 0:
            años_bisiestos.append(x)
            if x % 100 == 0 and not x % 400 == 0:
                años_bisiestos.remove(x)
    for x in range(año - 1, año + 29):
        if x in años_bisiestos:
            print(x)

bisiestos(2000)


