'''
CALENDARIO DE ADVIENTO
Crea una función que reciba un objeto de tipo "Date" y retorne lo siguiente:
 - Si la fecha coincide con el calendario de adviento 2023: Retornará el regalo de ese día (a tu elección).
 - Si la fecha es anterior: Cuánto queda para que comience el calendario.
 - Si la fecha es posterior: Cuánto tiempo ha pasado desde que ha finalizado.
Notas:
 - Tenemos en cuenta que cada día del calendario comienza a medianoche 00:00:00 y finaliza a las 23:59:59.
 - Debemos trabajar con fechas que tengan año, mes, día, horas, minutos y segundos.
'''
dict_regalos = {
  1 : 'Arbol',
  2 : 'Reno',
  3 : 'Estrella',
  4 : 'Copo',
  5 : 'Galletas',
  6 : 'Papa noel',
  7 : 'Rey mago',
  8 : 'Regalo',
  9 : 'Calcetín',
  10 : 'Gorro',
  11 : 'Guantes',
  12 : 'Roscón',
  13 : 'Arbol',
  14 : 'Reno',
  15 : 'Estrella',
  16 : 'Copo',
  17 : 'Galletas',
  18 : 'Papa noel',
  19 : 'Rey mago',
  20 : 'Regalo',
  21 : 'Calcetín',
  22 : 'Gorro',
  23 : 'Guantes',
  24 : 'Roscón',
}

from datetime import datetime
inicio_adviento = datetime(2023, 12, 1, 0, 0, 0)
inicio_adviento_stamp = inicio_adviento.timestamp()
final_adviento = datetime (2023, 12, 23, 23, 59, 59)
final_adviento_stamp = final_adviento.timestamp()
def adviento(fecha):
  fecha = datetime(fecha[0], fecha[1], fecha[2], fecha[3], fecha[4], fecha[5])
  fecha_stamp = fecha.timestamp()
  if inicio_adviento_stamp < fecha_stamp < final_adviento_stamp:
    if fecha.day in dict_regalos.keys():
      regalo = dict_regalos[fecha.day]
      print('Aqui tienes tu regalo,', regalo)
  elif fecha_stamp > final_adviento_stamp:
    retraso = fecha - final_adviento
    print('El calendario ha sido hace', retraso)
  elif fecha_stamp < inicio_adviento_stamp:
    tiempo_que_falta = inicio_adviento - fecha
    print('Faltan', tiempo_que_falta, 'para que empiece el calendario de adviento')
  
fechas = [2020, 4, 21, 11, 34, 23]
adviento(fechas)
fechas = [2024, 2, 21, 10, 23, 1]
adviento(fechas)
fechas = [2023, 12, 26, 2, 12, 1]
adviento(fechas)
fechas = [2023, 12, 21, 5, 2, 12]
adviento(fechas)
