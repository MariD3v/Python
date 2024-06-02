'''
TOP ALGORITMOS | QUICK SORT
Implementa uno de los algoritmos de ordenación más famosos: 
el "Quick Sort", creado por C.A.R. Hoare.
Dedícale tiempo a entenderlo, no únicamente a copiar su implementación.
'''
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    
    pivot = lista[len(lista) // 2]  # Elegimos el pivote (en este caso, el elemento del medio)
    left = [x for x in lista if x < pivot]  # Lista con elementos menores al pivote
    middle = [x for x in lista if x == pivot]  # Lista con elementos iguales al pivote
    right = [x for x in lista if x > pivot]  # Lista con elementos mayores al pivote
    
    return quicksort(left) + middle + quicksort(right)

lista_desordenada = [38, 27, 43, 3, 9, 82, 10]
lista_ordenada = quicksort(lista_desordenada)
print(lista_ordenada)
