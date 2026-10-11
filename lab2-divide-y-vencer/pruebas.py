"""Pruebas del subarreglo maximo."""
import random

from subarreglo import (
    subarreglo_fuerza_bruta,
    subarreglo_maximo,
    suma_cruzada,
)


def ambas(serie):
    """Devuelve las sumas de ambos algoritmos."""
    copia = list(serie)
    fb = subarreglo_fuerza_bruta(serie)[2]
    dv = subarreglo_maximo(serie, 0, len(serie) - 1)[2]
    assert serie == copia  # no modifica la lista
    return fb, dv


# Serie de ocho dias
assert ambas([-3, 5, -2, 8, -6, 3, 9, -4]) == (17, 17)
# Un solo elemento
assert ambas([7]) == (7, 7)
assert ambas([-7]) == (-7, -7)
# Todos negativos: gana el menos negativo
assert ambas([-5, -2, -9, -1, -8]) == (-1, -1)
# Todos positivos: suma total
assert ambas([1, 2, 3, 4, 5]) == (15, 15)
# Caso cruzado: el mejor tramo (indices 2..5) cruza el medio
serie = [-10, -10, 4, 5, 6, 7, -10, -10]
assert ambas(serie) == (22, 22)
assert suma_cruzada(serie, 0, 3, 7)[2] == 22

# Listas aleatorias
random.seed(42)
for _ in range(50):
    n = random.randint(1, 60)
    datos = [random.randint(-100, 100) for _ in range(n)]
    fb, dv = ambas(datos)
    assert fb == dv, (datos, fb, dv)

print("Todas las pruebas pasaron.")