"""
=============================================================
  COMPARACIÓN TÉCNICA: Algoritmos de Búsqueda
=============================================================
  Algoritmos comparados:
    1. Búsqueda Lineal      — O(n)
    2. Búsqueda Binaria     — O(log n)
    3. Búsqueda por Saltos  — O(√n)
    4. Búsqueda Interpolada — O(log log n) promedio
=============================================================
"""

import sys
import os
import time
import random

# Importar desde la carpeta busqueda/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "busqueda"))

from lineal        import busqueda_lineal
from binaria       import busqueda_binaria
from saltos        import busqueda_saltos
from interpolacion import busqueda_interpolacion


# ─────────────────────────────────────────────
#  UTILIDADES
# ─────────────────────────────────────────────

def cabecera(titulo):
    linea = "=" * 65
    print(f"\n{linea}")
    print(f"  {titulo}")
    print(linea)


def medir(func, lista, objetivo):
    inicio = time.perf_counter()
    idx, iteraciones = func(lista, objetivo)
    fin = time.perf_counter()
    return idx, iteraciones, (fin - inicio) * 1_000_000  # µs


ALGORITMOS = {
    "Lineal"        : busqueda_lineal,
    "Binaria"       : busqueda_binaria,
    "Saltos"        : busqueda_saltos,
    "Interpolación" : busqueda_interpolacion,
}

# Nota: binaria, saltos e interpolación requieren lista ordenada.
# Para comparación justa, siempre se le da una lista ordenada.


# ─────────────────────────────────────────────
#  PRUEBA 1: CORRECTITUD
# ─────────────────────────────────────────────

cabecera("PRUEBA 1 — Correctitud")

muestra  = sorted([64, 34, 25, 12, 22, 11, 90, 50, 77, 3])
objetivo = 50
esperado = muestra.index(objetivo)

print(f"\n  Lista ordenada : {muestra}")
print(f"  Buscando       : {objetivo}  (índice correcto = {esperado})\n")
print(f"  {'Algoritmo':<18}  {'Índice':>7}  {'Iteraciones':>12}  {'Correcto':>9}")
print(f"  {'-'*18}  {'-'*7}  {'-'*12}  {'-'*9}")

for nombre, func in ALGORITMOS.items():
    idx, its, _ = medir(func, muestra, objetivo)
    correcto = "✓ SÍ" if idx == esperado else "✗ NO"
    print(f"  {nombre:<18}  {idx:>7}  {its:>12}  {correcto:>9}")


# ─────────────────────────────────────────────
#  PRUEBA 2: RENDIMIENTO POR TAMAÑO
# ─────────────────────────────────────────────

cabecera("PRUEBA 2 — Tiempo de ejecución (µs) por tamaño de lista")

tamanos = [100, 1_000, 10_000, 100_000, 1_000_000]
nombres = list(ALGORITMOS.keys())

# Encabezado tabla
header = f"  {'Tamaño':>10}" + "".join(f"  {n:>14}" for n in nombres)
print(f"\n{header}")
print(f"  {'-'*10}" + "".join(f"  {'-'*14}" for _ in nombres))

for n in tamanos:
    datos     = sorted(random.sample(range(n * 10), n))
    objetivo  = datos[n // 2]  # elemento que existe (mediana)
    fila      = f"  {n:>10,}"
    for func in ALGORITMOS.values():
        _, _, us = medir(func, datos, objetivo)
        fila += f"  {us:>13.3f}µ"
    print(fila)


# ─────────────────────────────────────────────
#  PRUEBA 3: CONTEO DE ITERACIONES PROMEDIO
# ─────────────────────────────────────────────

cabecera("PRUEBA 3 — Iteraciones promedio (n=10 000, 50 búsquedas)")

N      = 10_000
REPS   = 50
datos  = sorted(random.sample(range(N * 5), N))

# 50 objetivos que SÍ existen
objetivos = random.sample(datos, REPS)

totales = {nombre: 0 for nombre in ALGORITMOS}

for obj in objetivos:
    for nombre, func in ALGORITMOS.items():
        _, its, _ = medir(func, datos, obj)
        totales[nombre] += its

print(f"\n  {'Algoritmo':<18}  {'Iter. promedio':>15}  {'Complejidad':>15}")
print(f"  {'-'*18}  {'-'*15}  {'-'*15}")

import math
esperadas = {
    "Lineal"        : f"O(n)  ≈ {N//2:,}",
    "Binaria"       : f"O(log n) ≈ {int(math.log2(N))}",
    "Saltos"        : f"O(√n)  ≈ {int(math.sqrt(N))}",
    "Interpolación" : f"O(log log n) ≈ {int(math.log2(math.log2(N)))}",
}

for nombre in ALGORITMOS:
    promedio = totales[nombre] / REPS
    print(f"  {nombre:<18}  {promedio:>15.1f}  {esperadas[nombre]:>15}")


# ─────────────────────────────────────────────
#  PRUEBA 4: CASOS EXTREMOS
# ─────────────────────────────────────────────

cabecera("PRUEBA 4 — Casos extremos")

casos = [
    ("Lista vacía",           [],                      5   ),
    ("Un elemento (existe)",  [42],                     42  ),
    ("Un elemento (no exist)", [42],                    99  ),
    ("Primer elemento",       list(range(1, 21)),       1   ),
    ("Último elemento",       list(range(1, 21)),       20  ),
    ("Elemento no existe",    list(range(1, 21)),       99  ),
    ("Todos iguales",         [7] * 10,                 7   ),
]

print(f"\n  {'Caso':<28}  {'Lineal':>7}  {'Binaria':>8}  {'Saltos':>7}  {'Interp.':>8}")
print(f"  {'-'*28}  {'-'*7}  {'-'*8}  {'-'*7}  {'-'*8}")

for desc, lista, obj in casos:
    resultados = []
    for func in ALGORITMOS.values():
        idx, _, _ = medir(func, lista, obj)
        resultados.append("✓" if idx != -1 else "–")
    print(f"  {desc:<28}  {'  '.join(f'{r:>6}' for r in resultados)}")


# ─────────────────────────────────────────────
#  RESUMEN FINAL
# ─────────────────────────────────────────────

cabecera("RESUMEN COMPARATIVO")

print("""
  ┌──────────────────┬──────────────┬──────────────┬──────────────┬──────────────┐
  │ Característica   │   Lineal     │   Binaria    │   Saltos     │ Interpolación│
  ├──────────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
  │ Complejidad      │    O(n)      │  O(log n)    │   O(√n)      │ O(log log n) │
  │ Lista ordenada   │    No        │    Sí        │    Sí        │     Sí       │
  │ Distribución     │ Cualquiera   │ Cualquiera   │ Cualquiera   │  Uniforme    │
  │ Implementación   │  Muy simple  │   Simple     │   Moderada   │  Compleja    │
  │ Mejor uso        │ Listas peq.  │  General     │  Medio/gde   │ Rang. unifm. │
  └──────────────────┴──────────────┴──────────────┴──────────────┴──────────────┘

  Recomendación según contexto:
    • Lista pequeña o sin ordenar    → Búsqueda Lineal
    • Lista ordenada, uso general    → Búsqueda Binaria  ← más confiable
    • Lista enorme, ordenada         → Búsqueda por Saltos
    • Datos numéricos muy uniformes  → Búsqueda por Interpolación
""")
