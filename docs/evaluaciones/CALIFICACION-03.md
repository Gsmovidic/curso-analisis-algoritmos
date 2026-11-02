# Retroalimentación — Laboratorio 03 Estructuras de datos

**Estudiante:** Victor Manuel Tobon Sepulveda · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `b423b01`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 0 / 20 |
| Calidad de la explicación teórica | 0 / 20 |
| Corrección de la implementación | 23 / 25 |
| Calidad del análisis de las gráficas | 12 / 25 |
| Documentación y organización del informe | 2 / 10 |
| **Total** | **37 / 100** |
| **Nota (0–5)** | **1.85** |

## 1. Corrección conceptual (0 / 20)
**Lo que puede mejorar (y cómo corregirlo):**
- El `README.md` publicado está vacío, así que las preguntas 3, 4 y 5 (colisiones, tabla hash frente a árbol, recomendación y estimación a 5.000.000 de envíos) no tienen respuesta.
  → *Cómo corregirlo:* escriba en el `README.md` la Parte 3 con sus propias palabras, una sección por pregunta, apoyándose en lo que midió.

## 2. Calidad de la explicación teórica (0 / 20)
**Lo que puede mejorar (y cómo corregirlo):**
- La pregunta 1 no está respondida: falta explicar por qué la lista cuesta `Θ(n)`, por qué la tabla cuesta `Θ(1 + α)`, el supuesto sobre la función hash y qué pasa si todas las guías caen en una casilla.
  → *Cómo corregirlo:* responda cada parte de la pregunta 1 en un párrafo propio; piense en cuántos nodos se recorren cuando la guía no existe.

## 3. Corrección de la implementación (23 / 25)
**Lo que hizo bien:**
- `ListaEnlazada` y `TablaHash` están completas, la tabla reutiliza la lista en cada casilla y no usa `dict`, `set` ni `hash()`.
- `buscar` usa un ciclo `while`, la colisión con `m = 7` funciona y `factor_carga` da 3/7.
- `pruebas.py` cubre búsquedas exitosas e infructuosas, la colisión, el factor de carga y 20 colecciones aleatorias; todas pasan.
- Tiene *type hints* y dos líneas en blanco entre funciones.

**Lo que puede mejorar (y cómo corregirlo):**
- Las funciones de `medicion.py` (incluida `generar_guias_inexistentes`) no tienen las secciones `Args` y `Returns` en su *docstring*.
  → *Cómo corregirlo:* agregue `Args:` y `Returns:` al estilo de `estructuras.py` en cada función.

## 4. Calidad del análisis de las gráficas (12 / 25)
**Lo que hizo bien:**
- Las dos gráficas existen, con título, ejes rotulados y leyenda. La primera usa seis valores de `n` con ambas curvas en los mismos ejes (la lista llega a unos 7.300 µs en n = 50.000 y la tabla queda cerca de 0). La segunda usa cinco valores de `α` entre 0,25 y 10.
- Las mediciones usan `time.perf_counter()` solo sobre las búsquedas, con 200 guías inexistentes y semilla fija.

**Lo que puede mejorar (y cómo corregirlo):**
- No hay análisis: la pregunta 2 (factores de crecimiento entre dos valores de `n` y comportamiento al subir `α`) no está escrita, y las gráficas no están incrustadas en ningún informe.
  → *Cómo corregirlo:* tome dos valores consecutivos de `n` de su gráfica, divida los tiempos y compare con lo esperado; luego describa la curva de `α`. Inserte las imágenes con `![texto](graficas/lista_vs_tabla.png)`.

## 5. Documentación y organización del informe (2 / 10)
**Lo que hizo bien:**
- La carpeta `lab3-estructuras-datos/` está bien ubicada y tiene los archivos pedidos; hay cuatro commits con mensajes descriptivos.

**Lo que puede mejorar (y cómo corregirlo):**
- El `README.md` está vacío: no tiene su nombre, instrucciones de reproducción, descripción de las partes, enlaces al código ni las gráficas visibles.
  → *Cómo corregirlo:* complete el `README.md` en el orden pedido y enlace `estructuras.py`, `pruebas.py` y `medicion.py` con `[estructuras.py](estructuras.py)`.
- El `requirements.txt` del laboratorio está guardado con una codificación que no se lee como texto normal.
  → *Cómo corregirlo:* regenérelo con `pip freeze > requirements.txt` desde una terminal que use UTF-8, o guárdelo como UTF-8 desde el editor.

## ¿El código funciona?
Sí. Las pruebas pasan, ambas estructuras devuelven lo mismo y las gráficas se generan con las mediciones. Lo que falta es el informe escrito.
