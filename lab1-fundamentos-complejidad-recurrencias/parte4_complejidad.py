"""Experimento de la Parte 4: Comparación entre Insertion Sort y Merge Sort."""

import os
import time
import matplotlib.pyplot as plt
from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


def ejecutar_experimento_p4():
    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]
    tiempos_insertion = []
    tiempos_merge = []

    os.makedirs("graficas", exist_ok=True)

    for n in tamanos:
        datos = generar_aleatorio(n, semilla=42)

        # Insertion Sort (mediana de 3 corridas)
        t_ins = []
        for _ in range(3):
            t0 = time.perf_counter()
            insertion_sort(datos)
            t1 = time.perf_counter()
            t_ins.append(t1 - t0)
        tiempos_insertion.append(sum(t_ins) / 3)

        # Merge Sort (mediana de 3 corridas)
        t_mer = []
        for _ in range(3):
            t0 = time.perf_counter()
            merge_sort(datos)
            t1 = time.perf_counter()
            t_mer.append(t1 - t0)
        tiempos_merge.append(sum(t_mer) / 3)

    plt.figure(figsize=(8, 5))
    plt.plot(
        tamanos,
        tiempos_insertion,
        marker="o",
        color="crimson",
        label="Insertion Sort (Escenario A)",
    )
    plt.plot(
        tamanos,
        tiempos_merge,
        marker="^",
        color="dodgerblue",
        label="Merge Sort (Escenario A)",
    )
    plt.title("Parte 4: Comparación de Tiempo de Ejecución (Escenario A)")
    plt.xlabel("Tamaño de Entrada (n)")
    plt.ylabel("Tiempo de Ejecución (segundos)")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficas/parte4_tiempo.png")
    plt.close()


if __name__ == "__main__":
    ejecutar_experimento_p4()