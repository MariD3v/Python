'''
CICLO SEXAGENARIO CHINO
Crea un función, que dado un año, indique el elemento 
y animal correspondiente en el ciclo sexagenario del zodíaco chino.
- Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
- El ciclo sexagenario se corresponde con la combinación de los elementos
  madera, fuego, tierra, metal, agua y los animales rata, buey, tigre,
  conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo
  (en este orden).
- Cada elemento se repite dos años seguidos.
- El último ciclo sexagenario comenzó en 1984 (Madera Rata).
'''
def sexagenario(año):
  lista_animales = ['rata', 'buey', 'tigre', 'conejo', 'dragón', 'serpiente', 'caballo', 'oveja', 'mono', 'gallo', 'perro', 'cerdo']
  lista_elementos = ['madera', 'fuego', 'tierra', 'metal', 'agua']
  if año < 604:
    return('El ciclo sexagenario chino comenzo a partir del 604')
  else:
    indice_año = (año - 4) % 600
    animal = lista_animales[indice_año % 12]
    elemento = lista_elementos[(indice_año % 10)//2]
    return (animal, elemento)

print(sexagenario(2000))
print(sexagenario(1998))
print(sexagenario(1971))
print(sexagenario(1996))
print(sexagenario(604))
print(sexagenario(1974))
