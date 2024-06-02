'''
MÁQUINA EXPENDEDORA 
Simula el funcionamiento de una máquina expendedora creando una operación
que reciba dinero (array de monedas) y un número que indique la selección del producto.
- El programa retornará el nombre del producto y un array con el dinero de vuelta (con el menor número de monedas).
- Si el dinero es insuficiente o el número de producto no existe, 
deberá indicarse con un mensaje y retornar todas las monedas.
- Si no hay dinero de vuelta, el array se retornará vacío.
- Para que resulte más simple, trabajaremos en céntimos con monedas de 5, 10, 50, 100 y 200.
- Debemos controlar que las monedas enviadas estén dentro de las soportadas.
'''

def expendedora(n_producto, dinero):
    if n_producto == 1:
        producto = 'Coca Cola' 
        precio = 10
    elif n_producto == 2:
        producto = 'Algodón de Azúcar'
        precio = 45
    elif n_producto == 3:
        producto = 'Petisuit'
        precio = 75
    elif n_producto == 4:
        producto = 'Batido de fresa'
        precio = 30

    if dinero < precio or n_producto > 4 or n_producto < 1:
        print('Dinero insuficiente o producto equivocado', dinero)
    else:
        lista_de_monedas = [5, 10, 50, 100, 200]
        vueltas = dinero - precio
        vueltas_monedas = []
        for x in reversed(lista_de_monedas):
            while vueltas >= x:
                vueltas_monedas.append(x)
                vueltas = vueltas - x

            else:
                continue
        print (producto, vueltas_monedas)

dinero = 50 + 100
expendedora(1, dinero)
dinero = 50 + 200
expendedora(3, dinero)
dinero = 50
expendedora(2, dinero)
dinero = 50 + 100
expendedora(4, dinero)
dinero = 20 + 50
