# Laboratorio 1 — Fundamentos, complejidad y recurrencias

**Nombre completo:** Victor Manuel Tobón Sepúlveda  
**Curso:** Análisis de Algoritmos  
**Fecha:** Septiembre 20 del 2026  

---

## Instrucciones para reproducir el experimento

```bash
# 1. Activar entorno virtual desde la raíz
.\venv\Scripts\Activate.ps1  # Windows PowerShell
# source venv/bin/activate   # Linux/macOS

# 2. Instalar dependencias e ingresar al laboratorio
pip install -r requirements.txt
cd lab1-fundamentos-complejidad-recurrencias

# 3. Ejecutar experimentos y generar gráficas
python parte3_casos.py        # Genera parte3_comparaciones.png y parte3_tiempo.png
python parte4_complejidad.py  # Genera parte4_tiempo.png



Parte 1 — Analizar el algoritmo antes de comprar hardwareTamiza incumple la restricción innegociable de la ventana temporal de 4 horas (02:00 a 06:00 a. m.).Un algoritmo puede ser correcto (retornar la lista ordenada de mayor a menor riesgo) pero ineficiente e inviable (sobrepasar el tiempo disponible). Al pasar de 20.000 a 1.200.000 registros, el tamaño $n$ aumenta por un factor de 60. Como Insertion Sort es cuadrático ($O(n^2)$), sus operaciones se multiplican por $60^2 = 3.600$.Duplicar la velocidad del servidor solo reduce el tiempo a la mitad (factor de 2), pasando la ejecución de 8.3 horas a unas 4.15 horas. El proceso sigue fallando porque el cuello de botella es asintótico y algorítmico, no de hardware.Ejemplo propio de algoritmo correcto pero inviableUn módulo de consolidación de inventario con 50.000 productos diseñado con un algoritmo $O(n^3)$. Para cumplir la regla de negocio debe finalizar en una latencia máxima de 30 minutos antes de abrir las tiendas. Aunque calcula correctamente los saldos, tarda más de 12 horas continuas con 50.000 ítems, resultando inoperable.