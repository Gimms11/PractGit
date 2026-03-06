# Algoritmo de Ordenación Rápida (Quick Sort)

def quick_sort(lista):
    # Caso base: listas de 0 o 1 elemento ya están ordenadas
    if len(lista) <= 1:
        return lista

    pivote = lista[len(lista) // 2]  # Elegir el pivote (elemento del medio)

    menores  = [x for x in lista if x < pivote]   # Elementos menores al pivote
    iguales  = [x for x in lista if x == pivote]  # Elementos iguales al pivote
    mayores  = [x for x in lista if x > pivote]   # Elementos mayores al pivote

    # Ordenar recursivamente y concatenar los tres grupos
    return quick_sort(menores) + iguales + quick_sort(mayores)


# --- Demostración ---
numeros = [3, 6, 8, 10, 1, 2, 1]
print("Lista original:  ", numeros)

ordenada = quick_sort(numeros)
print("Lista ordenada:  ", ordenada)
