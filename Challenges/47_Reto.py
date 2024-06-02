'''
EL DETECTOR DE HANDLES
Crea una función que sea capaz de detectar y retornar todos los
handles de un texto usando solamente Expresiones Regulares.
Debes crear una expresión regular para cada caso:
- Handle usuario: Los que comienzan por "@"
- Handle hashtag: Los que comienzan por "#"
- Handle web: Los que comienzan por "www." y finalizan con un dominio (.com, .es...)
'''
import re
def handles(texto):
    patron_usuario = r'@[a-zA-Z0-9-]+'
    patron_hashtag = r'\B#\w*[a-zA-Z]+\w*'
    patron_web = r'www\.[a-zA-Z0-9-._/?&=]+\.[a-zA-Z0-9-]+'
    
    print('Estos son los usuarios:', re.findall(patron_usuario, texto), '\nEstos son los hashtags:', re.findall(patron_hashtag, texto), '\nEstas son las webs:', re.findall(patron_web, texto))

handles('Yo soy @Mari o @LittleMari. Algún dia, haré un web de mi pasteleria www.pasteleriademari.com #Pasteles #MariPastelera #Programadora')