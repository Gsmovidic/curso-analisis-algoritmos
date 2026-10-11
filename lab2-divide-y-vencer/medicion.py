"""Medicion de tiempos: fuerza bruta vs divide y venceras."""
import random
import statistics
import time

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

TAMANOS = [10, 50, 100, 500, 1000, 2000, 4000, 8000]
REPETICIONES = 3
SEMILLA = 42


def medir(funcion, *args) -> float:
    """Devuelve la mediana (en segundos) de varias ejecuciones."""
    tiempos = []
    for _ in range(REPETICIONES):
        t0 = time.perf_counter()
        funcion(*args)
        tiempos.append(time.perf_counter() - t0)
    return statistics.median(tiempos)


def main() -> None:
    """Ejecuta el experimento y guarda la grafica."""
    random.seed(SEMILLA)
    t_fb, t_dv = [], []
    print(f"{'n':>6} {'fuerza bruta (ms)':>18} {'div. y venceras (ms)':>22}")
    for n in TAMANOS:
        datos = [random.randint(-100, 100) for _ in range(n)]
        suma_fb = subarreglo_fuerza_bruta(datos)[2]
        suma_dv = subarreglo_maximo(datos, 0, n - 1)[2]
        assert suma_fb == suma_dv, f"Sumas distintas en n={n}"
        t_fb.append(medir(subarreglo_fuerza_bruta, datos) * 1000)
        t_dv.append(medir(subarreglo_maximo, datos, 0, n - 1) * 1000)
        print(f"{n:>6} {t_fb[-1]:>18.4f} {t_dv[-1]:>22.4f}")

    plt.figure(figsize=(8, 5))
    plt.plot(TAMANOS, t_fb, marker="o", label="Fuerza bruta")
    plt.plot(TAMANOS, t_dv, marker="s", label="Divide y venceras")
    plt.title("Tiempo de ejecucion vs. tamano de entrada")
    plt.xlabel("Tamano de entrada n (dias)")
    plt.ylabel("Tiempo de ejecucion (ms)")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/tiempo_vs_n.png", dpi=150, bbox_inches="tight")


if __name__ == "__main__":
    main()