'''
Los Bucles/loops/ciclos sirven 
para pasar un mismo codigo varias veces
'''
#While (mientras que...)

condición = 0

while condición < 10: #Mientras que 'valor' = True, se ejecuta sin parar la función
    print('Mi condición es menor que 10') #Si queremos que el bucle no sea infinito, se hace el siguiente paso:
    condición += 2 #Cada vez que el bucle pasa por aqui, condición suma 2, por lo que este bucle se repetiria 5 veces, hasta llegar a 10.
else: #Si ya no se cumple, ejecuta 'x' función.
    print('Mi condición es igual que 10') 
while condición <20:
    print('Mi condición es menor que 20')
    condición += 2
    if condición == 12: #Si la condición llega a 12, ejecuta 'x' función.
        print('Mi condición es 12')
        break #Detiene el bucle al realizarse el 'if'.
print('El bucle ha terminado')

#For (Repite datos de listas, sets, tuplas y diccionarios. 
#Eliminando las ()y las '')

lista = ['Mari', 23, 1.70]

for datos in lista:
    print(datos)
    if datos == 'Mari':
        print('Este es mi nombre')
    if datos == 23:
        print('Esta es mi edad')
    if datos == 1.70:
        print('Esta es mi altura')
        break #Para el for. También impide que se ejecute el 'else'
else:         #Si termina el for, ejecuta 'x' función. 
    print('La lista ha terminado')

