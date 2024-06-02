#If (si...)
condición = True
if condición == True:
    print('Hola')

'''
Si 'variable'(condición) es True, 
entonces se ejecuta 'Función'(print)
'''
condición_1 = (2 + 3)
if condición_1 < 5:         #NO SE CUMPLE
    print('Es menor que 5')
if condición_1 > 5:         #NO SE CUMPLE
    print('Es mayor que 5')
if condición_1 == 5:        #SI SE CUMPLE
    print('Es igual que 5')

#Else (sino...)
'''
Else, siempre debe ir detrás de un If. (Nunca puede ir solo)
'''

if condición_1 < 5:         
    print('Es menor que 5') #NO SE CUMPLE
else:   #Al no cumplirse el if, se ejecuta la función del 'sino'
    print('Es mayor o igual que 5') #SI SE CUMPLE

#Elif (Sino, entonces comprueba esta condición)
'''
Elif, siempre debe ir detrás de un If. (Nunca puede ir solo)
'''
if condición_1 < 5:         
    print('Es menor que 5') #NO SE CUMPLE
elif condición_1 == 5:
    print('Es igual a 5') #SI SE CUMPLE
else:   
    print('Es mayor que 5') #NO SE CUMPLE

#Varias condiciones

if condición_1 < 10 and condición_1 > 3:         
    print('Es menor que 10 y mayor que 3') #SI SE CUMPLE
else:   
    print('Es mayor o igual que 10 o es menor o igual que 3') #NO SE CUMPLE

if condición_1 < 10 and not condición_1 > 3:         
    print('Es menor que 10 y menor o igual que 3') #NO SE CUMPLE
else:
    print('Es mayor o igual que 10 o es mayor que 3') #SE CUMPLE