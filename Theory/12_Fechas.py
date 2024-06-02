'''
Para crear fechas y horas debemos acceder 
al módulo datetime y a la función datetime
'''
#Fecha actual
from datetime import datetime
ahora = datetime.now()
print(ahora.day, '/', ahora.month, '/', ahora.year)
print(ahora.hour, ':', ahora.minute, ':', ahora.second)

#Fecha actual en timestamp
timestamp = ahora.timestamp() #Sirve para obtener un nº que representa el momento actual.
print(timestamp) 

#Fecha especifica
año_nuevo_2023 = datetime(2023, 1, 1)

'''
El módulo time, es una hora vacía donde nosotros
intruducimos datos (Horas, minutos y segundos).
'''
from datetime import time
hora = time(21, 6, 0) #Aqui metemos nuestros datos
print(hora.hour)
print(hora.minute)
print(hora.second)

'''
El módulo date, es una fecha vacía donde nosotros
intruducimos datos (Dia, mes y año).
'''

from datetime import date
fecha = date(2023, 4, 21)
print(fecha.year)
print(fecha.month)
print(fecha.day)

#Operar con fechas
#Para operar con fechas, las variables deben ser del mismo tipo (datetime, time o date)
diferencia_de_dias = ahora - año_nuevo_2023
print(diferencia_de_dias)

'''
timedelta, nos sirve para definir un espacio de tiempo
pero no una fecha concreta
'''
from datetime import timedelta
timedelta_1 = timedelta(0, 0, 0, 0, 1) # 1 minuto
timedelta_2 = timedelta(0, 30) # 30 segundos
print(timedelta_1 - timedelta_2)