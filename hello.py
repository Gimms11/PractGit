# Algoritmo de Ordenación Burbuja (Bubble Sort)

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        # En cada pasada, el elemento más grande "burbujea" al final
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiar elementos si están en el orden incorrecto
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


# --- Demostración ---
numeros = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:  ", numeros)

ordenada = bubble_sort(numeros)
print("Lista ordenada:  ", ordenada)
