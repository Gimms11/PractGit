# ──────────────────────────────────────────────
#  BÚSQUEDA POR INTERPOLACIÓN (Interpolation Search)
# ──────────────────────────────────────────────
#
#  Mejora la búsqueda binaria estimando la posición
#  probable del objetivo usando una fórmula lineal,
#  similar a cómo buscamos en un diccionario físico.
#
#  Fórmula del pivote:
#    pos = izq + ((obj - arr[izq]) * (der - izq)) /
#                (arr[der] - arr[izq])
#
#  Complejidad:
#    - Mejor caso  : O(1)
#    - Peor caso   : O(n)  → distribución muy no uniforme
#    - Promedio    : O(log log n)  → distribución uniforme
#  Requisito: la lista DEBE estar ordenada y con distribución
#             relativamente uniforme para buen rendimiento
# ──────────────────────────────────────────────

def busqueda_interpolacion(lista, objetivo):
    """
    Retorna el índice del objetivo si se encuentra,
    de lo contrario retorna -1.
    Incluye conteo de iteraciones.
    """
    izquierda = 0
    derecha = len(lista) - 1
    iteraciones = 0

    while (izquierda <= derecha
           and lista[izquierda] <= objetivo <= lista[derecha]):
        iteraciones += 1

        # Evitar división por cero
        if lista[derecha] == lista[izquierda]:
            if lista[izquierda] == objetivo:
                return izquierda, iteraciones
            break

        # Estimar posición probable
        pos = izquierda + (
            (objetivo - lista[izquierda]) * (derecha - izquierda)
            // (lista[derecha] - lista[izquierda])
        )

        if lista[pos] == objetivo:
            return pos, iteraciones
        elif lista[pos] < objetivo:
            izquierda = pos + 1
        else:
            derecha = pos - 1

    return -1, iteraciones


# ── Demo ──────────────────────────────────────
if __name__ == "__main__":
    datos = sorted([45, 12, 78, 3, 56, 99, 23, 67])
    objetivo = 56

    print("=== Búsqueda por Interpolación ===")
    print(f"Lista ordenada : {datos}")
    print(f"Buscando       : {objetivo}")

    idx, iteraciones = busqueda_interpolacion(datos, objetivo)
    if idx != -1:
        print(f"Encontrado en índice {idx} tras {iteraciones} iteración(es)")
    else:
        print(f"No encontrado tras {iteraciones} iteración(es)")

    idx2, it2 = busqueda_interpolacion(datos, 100)
    print(f"\nBuscando 100 → {'No encontrado' if idx2 == -1 else f'índice {idx2}'} ({it2} iteraciones)")
