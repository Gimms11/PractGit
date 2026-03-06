# ──────────────────────────────────────────────
#  BÚSQUEDA LINEAL (Linear Search)
# ──────────────────────────────────────────────
#
#  Recorre el array elemento por elemento hasta
#  encontrar el valor objetivo o agotar la lista.
#
#  Complejidad:
#    - Mejor caso  : O(1)  → el elemento es el primero
#    - Peor caso   : O(n)  → el elemento no existe o es el último
#    - Promedio    : O(n)
#  Requisito: la lista NO necesita estar ordenada
# ──────────────────────────────────────────────

def busqueda_lineal(lista, objetivo):
    """
    Retorna el índice del objetivo si se encuentra,
    de lo contrario retorna -1.
    Incluye conteo de iteraciones.
    """
    iteraciones = 0
    for i, elemento in enumerate(lista):
        iteraciones += 1
        if elemento == objetivo:
            return i, iteraciones
    return -1, iteraciones


# ── Demo ──────────────────────────────────────
if __name__ == "__main__":
    datos = [45, 12, 78, 3, 56, 99, 23, 67]
    objetivo = 56

    print("=== Búsqueda Lineal ===")
    print(f"Lista    : {datos}")
    print(f"Buscando : {objetivo}")

    idx, iteraciones = busqueda_lineal(datos, objetivo)
    if idx != -1:
        print(f"Encontrado en índice {idx} tras {iteraciones} iteración(es)")
    else:
        print(f"No encontrado tras {iteraciones} iteración(es)")

    # Caso: no existe
    idx2, it2 = busqueda_lineal(datos, 100)
    print(f"\nBuscando 100 → {'No encontrado' if idx2 == -1 else f'índice {idx2}'} ({it2} iteraciones)")
