# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Victor Manuel Tobón Sepúlveda · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-07 23:59 · **Versión revisada:** commit `15ec9fe`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 16 / 25 |
| Calidad de la explicación teórica | 8 / 25 |
| Corrección de la implementación | 16 / 20 |
| Calidad del análisis de las gráficas | 11 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **60 / 100** |
| **Nota (0–5)** | **3.00** |

## 1. Corrección conceptual (16 / 25)
**Lo que hizo bien:**
- Nombra la restricción que se incumple (la ventana de cuatro horas) y explica que un servidor el doble de rápido solo reduce el tiempo a la mitad.
- Da un segundo ejemplo propio (inventario de 50.000 productos) con cantidad de datos y límite de tiempo.
- En la Parte 2 identifica perjuicios al paciente, al operador y a la Secretaría, y dice quién asume el costo. También explica que el orden de la lista funciona como un triaje.

**Lo que puede mejorar:**
- No separa con claridad "el resultado es correcto" de "el resultado llega a tiempo"; la idea queda implícita.
- La cifra de "3.600 operaciones de más" no es exacta: el trabajo se multiplica por 3.600, no se suma.
- La dimensión ambiental es muy general: falta explicar cómo el tiempo de ejecución se vuelve consumo de energía y cuánto se acumula en años.

## 2. Calidad de la explicación teórica (8 / 25)
**Lo que hizo bien:**
- En 3.1 describe los tres casos, justifica que usaría el peor caso por la ventana estricta y deja escrita la predicción antes de medir.

**Lo que puede mejorar:**
- En 3.1 no dice sobre qué conjunto de entradas ni con qué tamaño se toma el máximo, el mínimo o el promedio.
- La Parte 4.1 está casi vacía: no plantea la recurrencia de merge sort `T(n) = 2T(n/2) + Θ(n)`, no explica de dónde sale cada término y no la resuelve por ningún método (árbol, sustitución o maestro).
- No calcula insertion sort línea a línea (cuántas veces se ejecuta cada línea) y no incluye la tabla de complejidades de mejor, peor y caso promedio.

## 3. Corrección de la implementación (16 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien de mayor a menor, no cambian la lista original, cuentan solo comparaciones entre elementos y no usan `sorted()` ni `list.sort()`. La mezcla de merge sort es propia y recursiva.
- Los tres generadores dan listas del tamaño pedido, con valores distintos, y la semilla hace los datos reproducibles. El orden de mayor a menor es consistente en todo el trabajo.

**Lo que puede mejorar:**
- Las funciones `ejecutar_experimento_p3` y `ejecutar_experimento_p4` no tienen *type hints* ni *docstring*. Las funciones internas `_merge_sort_rec` y `_mezclar` tampoco tienen *docstring*, y `algoritmos.py` no tiene descripción al inicio.

## 4. Calidad del análisis de las gráficas (11 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados, leyenda y las curvas pedidas en los mismos ejes.
- Identifica bien el peor caso (C), el mejor (B) y el intermedio (A), con las comparaciones medidas, y lo contrasta con su predicción.
- Recomienda merge sort, responde a la compra del servidor y declara que las cifras para 1.200.000 registros son estimaciones, explicando el factor de crecimiento.

**Lo que puede mejorar:**
- Las cifras del informe no coinciden con sus gráficas. En `parte4_tiempo.png` insertion sort llega a unos 3.6 segundos con 6.400 datos y merge sort a unos 0.04 segundos, pero el informe dice "casi un segundo" y usa 0,85 s y 0,012 s.
- Por eso las estimaciones (8,3 horas y 3,6 segundos) están mal ancladas a sus propios datos. Con lo que muestra la gráfica, insertion sort quedaría aún más lejos de la ventana de cuatro horas.
- En 4.2 no contrasta la conclusión con las complejidades de 4.1 (que no están calculadas) ni comenta qué pasa con los tamaños pequeños.
- En 4.3 falta una consideración distinta del tiempo (memoria extra de merge sort, estabilidad, mantenimiento) y no cita el tamaño de la gráfica de donde sale el dato del servidor.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Carpeta en la ubicación acordada, con todos los archivos y las tres gráficas. Las imágenes se ven en el informe y las partes 3 y 4 enlazan su código.
- Incluye su nombre, instrucciones para reproducir y 7 commits con mensajes descriptivos.

**Lo que puede mejorar:**
- Se publicaron las carpetas `__pycache__` aunque su `.gitignore` las excluye; conviene sacarlas del repositorio.
- El archivo `requirements.txt` quedó guardado con una codificación poco común (UTF-16); guárdelo como UTF-8.

## ¿El código funciona?
Sí. Los algoritmos ordenan correctamente, los generadores funcionan y los dos scripts corren sin errores y generan las tres gráficas.

## Para el próximo laboratorio
- Plantee y resuelva paso a paso las recurrencias, y calcule el costo línea a línea cuando se pida.
- Copie en el informe los valores que realmente muestran sus gráficas y use esos mismos datos para estimar tiempos.
- Defina los casos indicando el conjunto de entradas y el tamaño sobre los que se toma cada uno.
- Agregue *type hints* y *docstring* a todas las funciones, incluidas las internas.
- Desarrolle más la parte ambiental con una cuenta aproximada de energía acumulada.
