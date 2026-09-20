#Función de mayor a menor.
def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de índices de riesgo (de mayor a menor) usando inserción.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de índices de riesgo a ordenar.

    Returns:
        Tupla con la lista ordenada y el número de comparaciones entre elementos.
    """
    arr = datos.copy()
    comparaciones = 0
    n = len(arr)

    for i in range(1, n):
        clave = arr[i]
        j = i - 1
        
        # Cada evaluación en el while evalúa una comparación entre dos elementos
        while j >= 0:
            comparaciones += 1
            if arr[j] < clave:  # Orden descentente (mayor a menor)
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = clave

    return arr, comparaciones


#Función de ordenamiento por mezcla (merge sort)
def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de índices de riesgo (de mayor a menor) usando mezcla.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de índices de riesgo a ordenar.

    Returns:
        Tupla con la lista ordenada y el número de comparaciones entre elementos.
    """
    arr = datos.copy()

    def _merge_sort_rec(sub_arr: list[int]) -> tuple[list[int], int]:
        if len(sub_arr) <= 1:
            return sub_arr, 0

        medio = len(sub_arr) // 2
        izq, comp_izq = _merge_sort_rec(sub_arr[:medio])
        der, comp_der = _merge_sort_rec(sub_arr[medio:])

        mezclada, comp_mezcla = _mezclar(izq, der)
        return mezclada, comp_izq + comp_der + comp_mezcla

    def _mezclar(izq: list[int], der: list[int]) -> tuple[list[int], int]:
        resultado = []
        i = j = 0
        comparaciones = 0

        while i < len(izq) and j < len(der):
            comparaciones += 1
            if izq[i] >= der[j]:  # Conserva elementos mayores primero
                resultado.append(izq[i])
                i += 1
            else:
                resultado.append(der[j])
                j += 1

        resultado.extend(izq[i:])
        resultado.extend(der[j:])
        return resultado, comparaciones

    return _merge_sort_rec(arr)