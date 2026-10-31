import os
import random
import time
import matplotlib.pyplot as plt
from estructuras import ListaEnlazada, TablaHash


DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
CARPETA_GRAFICAS = os.path.join(DIRECTORIO_ACTUAL, "graficas")


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion."""
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def experimento_a() -> None:
    """Mide tiempo de busqueda de guias inexistentes frente a n."""
    valores_n = [100, 500, 1000, 5000, 20000, 50000]
    primos_m = [53, 251, 509, 2503, 10007, 25013]  # m cercano a n / 2, alpha approx 2

    tiempos_lista: list[float] = []
    tiempos_tabla: list[float] = []

    for n, m in zip(valores_n, primos_m):
        azar = random.Random(42 + n)
        existentes: set[int] = set()
        while len(existentes) < n:
            existentes.add(azar.randint(10**9, 10**10 - 1))

        lista = ListaEnlazada()
        tabla = TablaHash(m)

        for g in existentes:
            lista.insertar(g, "en bodega")
            tabla.insertar(g, "en bodega")

        # Verificación previa de consistencia
        muestra = random.sample(list(existentes), min(10, n))
        for g in muestra:
            assert lista.buscar(g) == tabla.buscar(g)

        inexistentes = generar_guias_inexistentes(existentes, 200, semilla=7)

        # Medición en Lista
        inicio = time.perf_counter()
        for g in inexistentes:
            lista.buscar(g)
        fin = time.perf_counter()
        tiempos_lista.append(((fin - inicio) / 200) * 1e6)  # en microsegundos

        # Medición en Tabla
        inicio = time.perf_counter()
        for g in inexistentes:
            tabla.buscar(g)
        fin = time.perf_counter()
        tiempos_tabla.append(((fin - inicio) / 200) * 1e6)  # en microsegundos

    # Graficar Experimento A
    plt.figure(figsize=(8, 5))
    plt.plot(valores_n, tiempos_lista, marker="o", label="Lista Enlazada")
    plt.plot(valores_n, tiempos_tabla, marker="s", label="Tabla Hash (α ≈ 2)")
    plt.title("Tiempo medio de búsqueda (guías inexistentes) vs n")
    plt.xlabel("Número de guías (n)")
    plt.ylabel("Tiempo medio por búsqueda (µs)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(CARPETA_GRAFICAS, "lista_vs_tabla.png"))
    plt.close()



def experimento_b() -> None:
    """Mide el tiempo de busqueda frente al factor de carga."""

    # Cantidad fija de guias para todos los experimentos.
    n = 20000

    # Diferentes tamaños de tabla para modificar el factor de carga.
    valores_m = [80021, 40009, 20011, 5003, 2003]

    # Generar las mismas guias para todos los experimentos.
    azar = random.Random(123)
    existentes: set[int] = set()

    while len(existentes) < n:
        existentes.add(azar.randint(10**9, 10**10 - 1))

    # Generar 200 guias que no existen.
    inexistentes = generar_guias_inexistentes(
        existentes, 200, semilla=7
    )

    # Construir la lista enlazada una sola vez.
    lista = ListaEnlazada()

    for guia in existentes:
        lista.insertar(guia, "en bodega")

    alfas_reales: list[float] = []
    tiempos_tabla: list[float] = []

    print("\nEXPERIMENTO B - EFECTO DEL FACTOR DE CARGA")
    print("-" * 55)

    for m in valores_m:

        # Construir una tabla con el tamaño actual.
        tabla = TablaHash(m)

        for guia in existentes:
            tabla.insertar(guia, "en bodega")

        # Registrar el factor de carga real.
        alfa = tabla.factor_carga()
        alfas_reales.append(alfa)

        # Verificar que ambas estructuras devuelvan lo mismo.
        muestra = azar.sample(list(existentes), 10)

        for guia in muestra:
            assert lista.buscar(guia) == tabla.buscar(guia), (
                f"Resultados diferentes para la guia {guia}"
            )

        # Medir únicamente las busquedas de guias inexistentes.
        inicio = time.perf_counter()

        for guia in inexistentes:
            tabla.buscar(guia)

        fin = time.perf_counter()

        tiempo_medio = ((fin - inicio) / 200) * 1e6
        tiempos_tabla.append(tiempo_medio)

        print(
            f"  Alpha: {alfa:6.2f} "
            f"| m: {m:6d} "
            f"| Tiempo: {tiempo_medio:10.4f} us "
            f"| Verificacion: OK"
        )

    # Graficar Experimento B.
    plt.figure(figsize=(8, 5))

    plt.plot(
        alfas_reales,
        tiempos_tabla,
        marker="d",
        color="red",
        label="Tabla Hash"
    )

    plt.title(
        "Tiempo medio de busqueda vs Factor de Carga "
        "(n = 20.000)"
    )
    plt.xlabel("Factor de carga (α = n / m)")
    plt.ylabel("Tiempo medio por busqueda (µs)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        os.path.join(CARPETA_GRAFICAS, "tiempo_vs_alfa.png")
    )
    plt.close()


if __name__ == "__main__":
    os.makedirs(CARPETA_GRAFICAS, exist_ok=True)
    experimento_a()
    experimento_b()
    print(f"Experimentos completados. Gráficas guardadas en: {CARPETA_GRAFICAS}")