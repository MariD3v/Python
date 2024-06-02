'''
Sirven para identificar nuestro código dentro de un ámbito de actuación
'''

class Persona: #La forma correcta de definir un clase es con Mayus sin _
    def __init__(self, nombre, apellido): #Aqui se establecen los datos de 'Persona'
        self.nombre = nombre #Estamos creando sus datos.
        self.apellido = apellido
    def hablar(self):   #Estamos creando funciones para persona.
        print('Está hablando')

marichuli = Persona('Mari', 'Salar')

print(marichuli.nombre)
marichuli.hablar()

