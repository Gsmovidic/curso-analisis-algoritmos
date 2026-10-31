import random

from estructuras import ListaEnlazada, TablaHash


def ejecutar_pruebas() -> None:
    """Ejecuta las pruebas de ListaEnlazada y TablaHash."""

    print("\n" + "=" * 55)
    print("       PRUEBAS - LISTA ENLAZADA Y TABLA HASH")
    print("=" * 55)

    # --------------------------------------------------
    # 1. PRUEBAS DE LISTA ENLAZADA
    # --------------------------------------------------
    print("\n[1] PRUEBAS DE LISTA ENLAZADA")

    lista = ListaEnlazada()

    lista.insertar(100, "en reparto")
    lista.insertar(200, "en bodega")

    assert lista.buscar(100) == "en reparto"
    print("  [OK] Busqueda exitosa de una guia.")

    assert lista.buscar(999) is None
    print("  [OK] Busqueda infructuosa de una guia.")

    # --------------------------------------------------
    # 2. PRUEBAS DE TABLA HASH
    # --------------------------------------------------
    print("\n[2] PRUEBAS DE TABLA HASH")

    tabla = TablaHash(7)

    tabla.insertar(10, "en bodega")
    tabla.insertar(24, "en reparto")
    tabla.insertar(17, "entregado")

    assert tabla.buscar(10) == "en bodega"
    assert tabla.buscar(24) == "en reparto"
    assert tabla.buscar(17) == "entregado"

    print("  [OK] Busqueda exitosa de las tres guias.")

    assert tabla.buscar(99) is None
    print("  [OK] Busqueda infructuosa de una guia.")

    # --------------------------------------------------
    # 3. VERIFICACION DE COLISIONES
    # --------------------------------------------------
    print("\n[3] PRUEBA DE COLISIONES")

    print("  Funcion hash: h(guia) = guia % 7")

    for guia in (10, 24, 17):
        print(f"  Guia {guia} -> Casilla {tabla.hash(guia)}")
        assert tabla.hash(guia) == 3

    assert tabla.casillas[3].tamano == 3

    print("  [OK] Las tres guias estan almacenadas en la casilla 3.")
    print("  [OK] Longitud de la lista de la casilla 3: 3.")

    # --------------------------------------------------
    # 4. FACTOR DE CARGA
    # --------------------------------------------------
    print("\n[4] PRUEBA DEL FACTOR DE CARGA")

    factor = tabla.factor_carga()

    assert factor == 3 / 7

    print(f"  Elementos almacenados: {tabla.tamano}")
    print(f"  Casillas disponibles: {tabla.m}")
    print(f"  Factor de carga: {factor:.4f}")
    print("  [OK] Factor de carga correcto.")

    # --------------------------------------------------
    # 5. PRUEBAS CON COLECCIONES ALEATORIAS
    # --------------------------------------------------
    print("\n[5] PRUEBAS CON 20 COLECCIONES ALEATORIAS")

    azar = random.Random(42)

    estados = [
        "en bodega",
        "en reparto",
        "entregado",
        "cancelado"
    ]

    total_busquedas = 0

    for numero in range(1, 21):

        n_elem = azar.randint(10, 100)
        m_casillas = azar.randint(5, 50)

        lista_test = ListaEnlazada()
        tabla_test = TablaHash(m_casillas)

        guias_existentes = set()

        while len(guias_existentes) < n_elem:
            guia = azar.randint(10**9, 10**10 - 1)
            guias_existentes.add(guia)

        # Insertar las mismas guias en ambas estructuras.
        for guia in guias_existentes:
            estado = azar.choice(estados)

            lista_test.insertar(guia, estado)
            tabla_test.insertar(guia, estado)

        # Verificar busquedas exitosas.
        for guia in guias_existentes:
            resultado_lista = lista_test.buscar(guia)
            resultado_tabla = tabla_test.buscar(guia)

            assert resultado_lista == resultado_tabla
            assert resultado_lista is not None

            total_busquedas += 1

        # Verificar busquedas infructuosas.
        guias_inexistentes = set()

        while len(guias_inexistentes) < 10:
            guia = azar.randint(10**9, 10**10 - 1)

            if guia not in guias_existentes:
                guias_inexistentes.add(guia)

        for guia in guias_inexistentes:
            resultado_lista = lista_test.buscar(guia)
            resultado_tabla = tabla_test.buscar(guia)

            assert resultado_lista == resultado_tabla
            assert resultado_lista is None

            total_busquedas += 1

        print(
            f"  [OK] Coleccion {numero:02d}/20 "
            f"| Guias: {n_elem:3d} "
            f"| Casillas: {m_casillas:2d}"
        )

    # --------------------------------------------------
    # RESULTADO FINAL
    # --------------------------------------------------
    print("\n" + "=" * 55)
    print("              RESULTADO DE LAS PRUEBAS")
    print("=" * 55)
    print("  [OK] Lista enlazada.")
    print("  [OK] Tabla hash.")
    print("  [OK] Colisiones por encadenamiento.")
    print("  [OK] Factor de carga.")
    print("  [OK] 20 colecciones aleatorias.")
    print(f"  [OK] {total_busquedas} comparaciones de busqueda.")
    print("\n  TODAS LAS PRUEBAS FUERON EXITOSAS.")
    print("=" * 55)


if __name__ == "__main__":
    ejecutar_pruebas()