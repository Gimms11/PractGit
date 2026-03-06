# ──────────────────────────────────────────────
#  BÚSQUEDA BINARIA (Binary Search)
# ──────────────────────────────────────────────
#
#  Divide el array por la mitad en cada paso.
#  Compara el elemento central con el objetivo
#  y descarta la mitad que no puede contenerlo.
#
#  Complejidad:
#    - Mejor caso  : O(1)  → el pivote es el objetivo
#    - Peor caso   : O(log n)
#    - Promedio    : O(log n)
#  Requisito: la lista DEBE estar ordenada
# ──────────────────────────────────────────────

def busqueda_binaria(lista, objetivo):
    """
    Retorna el índice del objetivo si se encuentra,
    de lo contrario retorna -1.
    Incluye conteo de iteraciones.
    """
    izquierda = 0
    derecha = len(lista) - 1
    iteraciones = 0

    while izquierda <= derecha:
        iteraciones += 1
        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:
            return medio, iteraciones
        elif lista[medio] < objetivo:
            izquierda = medio + 1   # Buscar en la mitad derecha
        else:
            derecha = medio - 1     # Buscar en la mitad izquierda

    return -1, iteraciones


# ── Demo ──────────────────────────────────────
if __name__ == "__main__":
    datos = sorted([45, 12, 78, 3, 56, 99, 23, 67])  # DEBE estar ordenada
    objetivo = 56

    print("=== Búsqueda Binaria ===")
    print(f"Lista ordenada : {datos}")
    print(f"Buscando       : {objetivo}")

    idx, iteraciones = busqueda_binaria(datos, objetivo)
    if idx != -1:
        print(f"Encontrado en índice {idx} tras {iteraciones} iteración(es)")
    else:
        print(f"No encontrado tras {iteraciones} iteración(es)")

    # Caso: no existe
    idx2, it2 = busqueda_binaria(datos, 100)
    print(f"\nBuscando 100 → {'No encontrado' if idx2 == -1 else f'índice {idx2}'} ({it2} iteraciones)")
