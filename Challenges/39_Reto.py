'''
LA LEY DE OHM
Crea una función que calcule el valor del parámetro perdido 
correspondiente a la ley de Ohm.
- Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
 el valor del tercero (redondeado a 2 decimales).
- Si los parámetros son incorrectos o insuficientes, la función retornará
 la cadena de texto "Invalid values".
 V = R*I
'''

def OHM(V = None, R = None, I= None):
    num_parametros = sum(parametros is not None for parametros in [V,R,I])
    if num_parametros != 2:
        print('Introduce 2 parametros')
    elif I == None:
        I = round(V/R, 2)
        return I
    elif R == None:
        R = round(V/I, 2)
        return R
    elif V == None:
        V = round(R*I, 2)
        return V
    
print(OHM(3, 4))