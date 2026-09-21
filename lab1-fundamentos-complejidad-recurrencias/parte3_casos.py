"""Experimento de la Parte 3: Evaluación de Insertion Sort en Escenarios A, B y C."""

import os
import time
import matplotlib.pyplot as plt
from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso


def ejecutar_experimento_p3():
    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]
    escenarios = {
        "A (Aleatorio)": generar_aleatorio,
        "B (Casi Ordenado)": generar_casi_ordenado,
        "C (Orden Inverso)": generar_inverso,
    }

    resultados_comp = {e: [] for e in escenarios}
    resultados_tiempo = {e: [] for e in escenarios}

    os.makedirs("graficas", exist_ok=True)

    for nombre, generador in escenarios.items():
        for n in tamanos:
            tiempos = []
            comparaciones_lista = []

            for i in range(3):
                # Generamos una lista nueva usando semillas distintas por corrida
                # para que no reutilice la lista que ya fue ordenada
                if nombre == "C (Orden Inverso)":
                    datos = generador(n)
                else:
                    datos = generador(n, semilla=42 + i)

                t_inicio = time.perf_counter()
                _, comp = insertion_sort(datos)
                t_fin = time.perf_counter()

                tiempos.append(t_fin - t_inicio)
                comparaciones_lista.append(comp)

            # Guardamos el promedio del tiempo y de las comparaciones
            resultados_comp[nombre].append(
                sum(comparaciones_lista) / len(comparaciones_lista)
            )
            resultados_tiempo[nombre].append(sum(tiempos) / len(tiempos))

    # Gráfica 1: Comparaciones
    plt.figure(figsize=(8, 5))
    for nombre in escenarios:
        plt.plot(tamanos, resultados_comp[nombre], marker="o", label=nombre)
    plt.title("Parte 3: Comparaciones vs. Tamaño de Entrada (Insertion Sort)")
    plt.xlabel("Tamaño de Entrada (n)")
    plt.ylabel("Número de Comparaciones")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficas/parte3_comparaciones.png")
    plt.close()

    # Gráfica 2: Tiempo
    plt.figure(figsize=(8, 5))
    for nombre in escenarios:
        plt.plot(tamanos, resultados_tiempo[nombre], marker="s", label=nombre)
    plt.title(
        "Parte 3: Tiempo de Ejecución vs. Tamaño de Entrada (Insertion Sort)"
    )
    plt.xlabel("Tamaño de Entrada (n)")
    plt.ylabel("Tiempo de Ejecución (segundos)")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficas/parte3_tiempo.png")
    plt.close()


if __name__ == "__main__":
    print("Iniciando experimento de la Parte 3...")
    ejecutar_experimento_p3()
    print(
        "✓ Experimento 3 finalizado. Revisa la carpeta 'graficas/'."
    )