# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Victor Manuel Tobon Sepulveda · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `f0a30d3`

Muy buen trabajo: el código es correcto y sus mediciones respaldan lo que usted afirma.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 17 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 22 / 25 |
| Calidad del análisis de las gráficas | 24 / 25 |
| Documentación y organización del informe | 5 / 10 |
| **Total** | **86 / 100** |
| **Nota (0–5)** | **4.30** |

## 1. Corrección conceptual (17 / 20)
**Lo que hizo bien:**
- Identifica que desde n=100 divide y vencerás gana y apoya la afirmación con cifras (17 veces más rápido en n=1000).
- Compara bien con el máximo de un arreglo: combinar cuesta una sola comparación, la recurrencia da `Θ(n)` y dividir no ayuda.
- Recomienda divide y vencerás y declara que lo de 1.000.000 de registros es una estimación, sin usar una regla de tres lineal.

**Lo que puede mejorar:**
- En la pregunta 3 no explica por qué la fuerza bruta gana en tamaños muy pequeños (el costo de las llamadas recursivas). Además quedó un "..." suelto.
- La recomendación de la pregunta 5 se apoya solo en los tiempos; faltó mencionar por qué importa para series de cientos de miles de registros.

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` y explica de dónde sale cada término.
- Aplica el método maestro y verifica que `n^(log₂2) = n` coincide con `Θ(n)`, así que es el caso 2 y da `Θ(n log n)`.
- Justifica el `Θ(n²)` de la fuerza bruta contando los pares de días.

**Lo que puede mejorar:**
- Podría mostrar el paso de la fórmula del método maestro (valores de a, b y f(n)) de forma más explícita.

## 3. Corrección de la implementación (22 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden entre sí en listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos y no llama a la fuerza bruta; ninguna función modifica la lista.
- El código cumple PEP 8 y las funciones principales tienen *docstrings* y *type hints*.

**Lo que puede mejorar:**
- La función `medir` de `medicion.py` no tiene *type hints* en sus parámetros ni la sección de argumentos en el *docstring*.

## 4. Calidad del análisis de las gráficas (24 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y 8 tamaños. El tiempo de la fuerza bruta en n=8000 (cerca de 2900 ms) coincide con lo que usted escribe.
- Calcula el factor al duplicar n en cuatro pares de tamaños (cerca de 4 para fuerza bruta y 2 para divide y vencerás) y lo compara con lo esperado.
- Agrega una tabla de valores medidos, que ayuda a ver los tamaños pequeños.

**Lo que puede mejorar:**
- Sobre el factor de `Θ(n log n)` conviene decir que es un poco mayor que 2 y no exactamente 2.

## 5. Documentación y organización del informe (5 / 10)
**Lo que hizo bien:**
- Siguió la estructura de carpetas pedida, enlazó el código en cada parte y las gráficas se ven en el informe.

**Lo que puede mejorar:**
- Faltan las instrucciones para reproducir: cómo activar el entorno y qué comandos ejecutar para las pruebas y la medición.
- Solo hay un commit para este laboratorio y se piden al menos tres, descriptivos y frecuentes.
- Quedó publicada la carpeta `__pycache__` del laboratorio 1; conviene que el `.gitignore` funcione para evitarlo.

## ¿El código funciona?
Sí. Las pruebas pasan y la medición corre completa, mostrando que ambos algoritmos dan la misma suma en cada tamaño.

## Para el próximo laboratorio
- Incluya al inicio del informe los pasos exactos para reproducir el experimento.
- Haga commits pequeños y frecuentes (al menos tres) con mensajes descriptivos.
- Complete los *type hints* y *docstrings* de todas las funciones, incluidas las auxiliares.
- Explique el porqué de cada resultado, no solo la cifra.
