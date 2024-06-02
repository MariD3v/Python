'''
Manejo de errores
'''

numero_1 = 2
numero_2 = '3'

#Try/Except

try: #Se ejecuta si no se produce un error
    print(numero_1 + numero_2)
    print('No se ha producido un error')
except: #Se ejecuta si se ha producido un error
    print('Se ha producido un error')

#Try/Except/Else

try: #Se ejecuta si no se produce un error
    print(numero_1 + numero_2)
    print('No se ha producido un error')
except:#Se ejecuta si se ha producido un error
    print('Se ha producido un error')
else: #Se ejecuta si no se produce un error #OPCIONAL
    print('La ejecución continua correctamente')

#Try/Except/Else/Finally

try: #Se ejecuta si no se produce un error
    print(numero_1 + numero_2)
    print('No se ha producido un error')
except:#Se ejecuta si se ha producido un error
    print('Se ha producido un error')
else: #Se ejecuta si no se produce un error #OPCIONAL
    print('La ejecución continua correctamente')
finally:#Se ejecuta siempre #OPCIONAL
    print('La ejecución continua')

#Tipo de errores

try: 
    print(numero_1 + numero_2)
    print('No se ha producido un error')
except ValueError:
    print('Se ha producido un ValueError')
except TypeError:
    print('Se ha producido un TypeError')

#Obtener información del error

try: 
    print(numero_1 + numero_2)
    print('No se ha producido un error')
except Exception as error:
    print(error) #Hemos guardado el error obtenido en la variable 'error'