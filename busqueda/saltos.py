# ──────────────────────────────────────────────
#  BÚSQUEDA POR SALTOS (Jump Search)
# ──────────────────────────────────────────────
#
#  Salta bloques de tamaño √n hasta que el
#  elemento del bloque supera al objetivo, luego
#  hace una búsqueda lineal hacia atrás.
#
#  Complejidad:
#    - Mejor caso  : O(1)
#    - Peor caso   : O(√n)
#    - Promedio    : O(√n)
#  Requisito: la lista DEBE estar ordenada
# ──────────────────────────────────────────────

import math

def busqueda_saltos(lista, objetivo):
    """
    Retorna el índice del objetivo si se encuentra,
    de lo contrario retorna -1.
    Incluye conteo de iteraciones.
    """
    n = len(lista)
    paso = int(math.sqrt(n))   # Tamaño del bloque = √n
    anterior = 0
    iteraciones = 0

    # Saltar bloques hasta superar el objetivo
    while anterior < n and lista[min(paso, n) - 1] < objetivo:
        iteraciones += 1
        anterior = paso
        paso += int(math.sqrt(n))
        if anterior >= n:
            return -1, iteraciones

    # Búsqueda lineal hacia atrás dentro del bloque
    while anterior < min(paso, n):
        iteraciones += 1
        if lista[anterior] == objetivo:
            return anterior, iteraciones
        anterior += 1

    return -1, iteraciones


# ── Demo ──────────────────────────────────────
if __name__ == "__main__":
    datos = sorted([45, 12, 78, 3, 56, 99, 23, 67])
    objetivo = 56

    print("=== Búsqueda por Saltos ===")
    print(f"Lista ordenada : {datos}")
    print(f"Tamaño bloque  : √{len(datos)} ≈ {int(math.sqrt(len(datos)))}")
    print(f"Buscando       : {objetivo}")

    idx, iteraciones = busqueda_saltos(datos, objetivo)
    if idx != -1:
        print(f"Encontrado en índice {idx} tras {iteraciones} iteración(es)")
    else:
        print(f"No encontrado tras {iteraciones} iteración(es)")

    idx2, it2 = busqueda_saltos(datos, 100)
    print(f"\nBuscando 100 → {'No encontrado' if idx2 == -1 else f'índice {idx2}'} ({it2} iteraciones)")
