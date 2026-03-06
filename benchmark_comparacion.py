"""
=============================================================
  COMPARACIÓN TÉCNICA: Bubble Sort  vs  Quick Sort
=============================================================
  Pruebas:
    1. Correctitud (mismo resultado ambos algoritmos)
    2. Rendimiento (tiempo de ejecución por tamaño)
    3. Conteo de operaciones (comparaciones e intercambios)
    4. Casos extremos (lista vacía, un elemento, ya ordenada,
       orden inverso, duplicados)
=============================================================
"""

import time
import random
import copy


# ─────────────────────────────────────────────
#  IMPLEMENTACIONES CON CONTEO DE OPERACIONES
# ─────────────────────────────────────────────

def bubble_sort(lista):
    """Bubble Sort — O(n²) promedio y peor caso."""
    arr = lista[:]
    n = len(arr)
    comparaciones = 0
    intercambios = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            comparaciones += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambios += 1

    return arr, comparaciones, intercambios


def quick_sort(lista):
    """Quick Sort — O(n log n) promedio, O(n²) peor caso."""
    ops = {"comparaciones": 0, "intercambios": 0}

    def _qs(arr):
        if len(arr) <= 1:
            return arr
        pivote = arr[len(arr) // 2]
        menores, iguales, mayores = [], [], []
        for x in arr:
            ops["comparaciones"] += 1
            if x < pivote:
                menores.append(x)
                ops["intercambios"] += 1
            elif x == pivote:
                iguales.append(x)
            else:
                mayores.append(x)
                ops["intercambios"] += 1
        return _qs(menores) + iguales + _qs(mayores)

    resultado = _qs(lista[:])
    return resultado, ops["comparaciones"], ops["intercambios"]


# ─────────────────────────────────────────────
#  UTILIDADES
# ─────────────────────────────────────────────

def medir_tiempo(func, lista):
    inicio = time.perf_counter()
    resultado, comp, swap = func(lista)
    fin = time.perf_counter()
    return resultado, comp, swap, (fin - inicio) * 1_000  # en milisegundos


def cabecera(titulo):
    linea = "=" * 60
    print(f"\n{linea}")
    print(f"  {titulo}")
    print(linea)


# ─────────────────────────────────────────────
#  PRUEBA 1: CORRECTITUD
# ─────────────────────────────────────────────

cabecera("PRUEBA 1 — Correctitud")

muestra = [42, 7, 19, 3, 55, 1, 28, 14]
res_bubble, *_ = bubble_sort(muestra)
res_quick,  *_ = quick_sort(muestra)
referencia = sorted(muestra)

print(f"  Lista original : {muestra}")
print(f"  Bubble Sort    : {res_bubble}")
print(f"  Quick Sort     : {res_quick}")
print(f"  sorted() Python: {referencia}")
print(f"\n  ¿Bubble == referencia? {'✓ SÍ' if res_bubble == referencia else '✗ NO'}")
print(f"  ¿Quick  == referencia? {'✓ SÍ' if res_quick  == referencia else '✗ NO'}")


# ─────────────────────────────────────────────
#  PRUEBA 2: RENDIMIENTO POR TAMAÑO
# ─────────────────────────────────────────────

cabecera("PRUEBA 2 — Rendimiento (tiempo en ms)")

print(f"\n  {'Tamaño':>8}  {'Bubble (ms)':>12}  {'Quick (ms)':>11}  {'Ganador':>10}")
print(f"  {'-'*8}  {'-'*12}  {'-'*11}  {'-'*10}")

for n in [100, 500, 1_000, 5_000, 10_000]:
    datos = [random.randint(0, 10_000) for _ in range(n)]
    _, _, _, t_bubble = medir_tiempo(bubble_sort, datos)
    _, _, _, t_quick  = medir_tiempo(quick_sort,  datos)
    ganador = "Quick Sort" if t_quick < t_bubble else "Bubble Sort"
    print(f"  {n:>8}  {t_bubble:>12.4f}  {t_quick:>11.4f}  {ganador:>10}")


# ─────────────────────────────────────────────
#  PRUEBA 3: CONTEO DE OPERACIONES
# ─────────────────────────────────────────────

cabecera("PRUEBA 3 — Conteo de operaciones (n=1 000)")

datos_op = [random.randint(0, 10_000) for _ in range(1_000)]

_, b_comp, b_swap, _ = medir_tiempo(bubble_sort, datos_op)
_, q_comp, q_swap, _ = medir_tiempo(quick_sort,  datos_op)

print(f"\n  {'Métrica':<22}  {'Bubble Sort':>12}  {'Quick Sort':>12}")
print(f"  {'-'*22}  {'-'*12}  {'-'*12}")
print(f"  {'Comparaciones':<22}  {b_comp:>12,}  {q_comp:>12,}")
print(f"  {'Movimientos/intercambios':<22}  {b_swap:>12,}  {q_swap:>12,}")


# ─────────────────────────────────────────────
#  PRUEBA 4: CASOS EXTREMOS
# ─────────────────────────────────────────────

cabecera("PRUEBA 4 — Casos extremos")

casos = {
    "Lista vacía"          : [],
    "Un elemento"          : [99],
    "Ya ordenada (asc)"    : list(range(1, 11)),
    "Orden inverso (desc)" : list(range(10, 0, -1)),
    "Todos duplicados"     : [5] * 8,
    "Con negativos"        : [-3, 7, -1, 4, 0, -9, 2],
}

for nombre, caso in casos.items():
    rb, *_ = bubble_sort(caso)
    rq, *_ = quick_sort(caso)
    ref    = sorted(caso)
    ok     = "✓" if rb == ref == rq else "✗"
    print(f"  {ok} {nombre:<25} → {rq}")


# ─────────────────────────────────────────────
#  RESUMEN FINAL
# ─────────────────────────────────────────────

cabecera("RESUMEN COMPARATIVO")

print("""
  ┌──────────────────┬──────────────────┬──────────────────┐
  │ Característica   │   Bubble Sort    │   Quick Sort     │
  ├──────────────────┼──────────────────┼──────────────────┤
  │ Mejor caso       │    O(n)          │   O(n log n)     │
  │ Caso promedio    │    O(n²)         │   O(n log n)     │
  │ Peor caso        │    O(n²)         │   O(n²)          │
  │ Espacio extra    │    O(1)          │   O(log n)       │
  │ Estable          │    Sí            │   No (esta impl) │
  │ Uso práctico     │ Didáctico/peq.   │ General/grande   │
  └──────────────────┴──────────────────┴──────────────────┘

  Conclusión: Quick Sort es significativamente más rápido en
  listas de gran tamaño. Bubble Sort sólo es competitivo en
  listas muy pequeñas o ya casi ordenadas.
""")
