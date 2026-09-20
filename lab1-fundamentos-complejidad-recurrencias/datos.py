"""Generadores de lotes de registros para los escenarios de Tamiza."""

import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    random.seed(semilla)
    datos = list(range(1, n + 1))
    random.shuffle(datos)
    return datos


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% desordenado al final (escenario B).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos (de mayor a menor en el 98%).
    """
    random.seed(semilla)
    n_ordenado = int(n * 0.98)
    n_restante = n - n_ordenado

    # Primer 98% en orden descendente (de mayor a menor)
    ordenados = list(range(n, n - n_ordenado, -1))

    # 2% restante desordenado al final
    restantes = list(range(1, n_restante + 1))
    random.shuffle(restantes)

    return ordenados + restantes


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en orden estrictamente inverso (escenario C: menor a mayor).

    Args:
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo de menor a mayor.
    """
    return list(range(1, n + 1))