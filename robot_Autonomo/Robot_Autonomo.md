# Navegación de Robot Autónomo mediante Geometría Computacional

Este documento presenta el cálculo de determinantes de orientación en el plano $\mathbb{R}^2$, la clasificación geométrica de giros, la lógica de decisión de navegación para un robot autónomo, la implementación en Python y el análisis de complejidad temporal $T(n)$.

---

## 1. Modelo Matemático y Criterio de Decisión

Para determinar hacia dónde debe girar un robot autónomo dentro de una bodega, se evalúan tres puntos ordenados en el plano cartesiano:

- $a(x_a, y_a)$: Posición actual.
- $b(x_b, y_b)$: Punto objetivo intermedio.
- $c(x_c, y_c)$: Punto de destino.

La orientación del trayecto $a \to b \to c$ se obtiene mediante el determinante:

$$\Delta = (x_b - x_a)(y_c - y_a) - (y_b - y_a)(x_c - x_a)$$

### Clasificación Geométrica y Decisión del Robot

| Condición del Determinante | Orientación | Decisión de Giro del Robot |
| :---: | :--- | :--- |
| $\Delta > 0$ | **Antihorario** | Girar hacia la izquierda |
| $\Delta < 0$ | **Horario** | Girar hacia la derecha |
| $\Delta = 0$ | **Colineal** | Continuar en línea recta (sin girar) |

---

## 2. Cálculo Paso a Paso por Caso

### **Caso 1:** $a(4, 2)$, $b(5, 3)$, $c(3, 7)$

1. Sustitución en la fórmula del determinante:
   $$\Delta_1 = (5 - 4)(7 - 2) - (3 - 2)(3 - 4)$$
2. Operaciones aritméticas:
   $$\Delta_1 = (1)(5) - (1)(-1) = 5 - (-1) = 5 + 1 = 6$$
3. **Clasificación:** Como $\Delta_1 = 6 > 0$, la orientación es **Antihorario**.
4. **Decisión del robot:** Girar hacia la **izquierda**.

---

### **Caso 2:** $a(2, 7)$, $b(6, 5)$, $c(8, 2)$

1. Sustitución en la fórmula del determinante:
   $$\Delta_2 = (6 - 2)(2 - 7) - (5 - 7)(8 - 2)$$
2. Operaciones aritméticas:
   $$\Delta_2 = (4)(-5) - (-2)(6) = -20 - (-12) = -20 + 12 = -8$$
3. **Clasificación:** Como $\Delta_2 = -8 < 0$, la orientación es **Horario**.
4. **Decisión del robot:** Girar hacia la **derecha**.

---

### **Caso 3:** $a(1, 7)$, $b(3, 3)$, $c(6, 6)$

1. Sustitución en la fórmula del determinante:
   $$\Delta_3 = (3 - 1)(6 - 7) - (3 - 7)(6 - 1)$$
2. Operaciones aritméticas:
   $$\Delta_3 = (2)(-1) - (-4)(5) = -2 - (-20) = -2 + 20 = 18$$
3. **Clasificación:** Como $\Delta_3 = 18 > 0$, la orientación es **Antihorario**.
4. **Decisión del robot:** Girar hacia la **izquierda**.

---

### **Caso 4:** $a(0, 4)$, $b(5, 4)$, $c(3, 1)$

1. Sustitución en la fórmula del determinante:
   $$\Delta_4 = (5 - 0)(1 - 4) - (4 - 4)(3 - 0)$$
2. Operaciones aritméticas:
   $$\Delta_4 = (5)(-3) - (0)(3) = -15 - 0 = -15$$
3. **Clasificación:** Como $\Delta_4 = -15 < 0$, la orientación es **Horario**.
4. **Decisión del robot:** Girar hacia la **derecha**.

---

### Tabla Resumen de Resultados

| Caso | Punto $a$ | Punto $b$ | Punto $c$ | Determinante ($\Delta$) | Orientación | Decisión del Robot |
| :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **Caso 1** | $(4, 2)$ | $(5, 3)$ | $(3, 7)$ | $6$ | Antihorario | Girar a la izquierda |
| **Caso 2** | $(2, 7)$ | $(6, 5)$ | $(8, 2)$ | $-8$ | Horario | Girar a la derecha |
| **Caso 3** | $(1, 7)$ | $(3, 3)$ | $(6, 6)$ | $18$ | Antihorario | Girar a la izquierda |
| **Caso 4** | $(0, 4)$ | $(5, 4)$ | $(3, 1)$ | $-15$ | Horario | Girar a la derecha |

---

## 3. Implementación en Python

El código fuente completo se encuentra en el archivo `orientacion_robot.py`:

```python
from typing import Tuple


def determinar_orientacion(
    a: Tuple[float, float],
    b: Tuple[float, float],
    c: Tuple[float, float],
) -> str:
    """
    Calcula el determinante (xb - xa)(yc - ya) - (yb - ya)(xc - xa)
    y retorna la orientacion geometrica: 'Antihorario', 'Horario' o 'Colineal'.
    """
    xa, ya = a
    xb, yb = b
    xc, yc = c

    det = (xb - xa) * (yc - ya) - (yb - ya) * (xc - xa)

    if det > 0:
        return "Antihorario"
    elif det < 0:
        return "Horario"
    else:
        return "Colineal"


def decidir_giro_robot(
    a: Tuple[float, float],
    b: Tuple[float, float],
    c: Tuple[float, float],
) -> Tuple[float, str, str]:
    """
    Evalua los tres puntos de navegacion y retorna el determinante,
    la orientacion y la accion de direccion que debe ejecutar el robot.
    """
    xa, ya = a
    xb, yb = b
    xc, yc = c
    det = (xb - xa) * (yc - ya) - (yb - ya) * (xc - xa)

    orientacion = determinar_orientacion(a, b, c)

    if orientacion == "Antihorario":
        decision = "Girar a la izquierda"
    elif orientacion == "Horario":
        decision = "Girar a la derecha"
    else:
        decision = "Continuar en linea recta (sin girar)"

    return det, orientacion, decision
```

### Ejecución

```bash
python orientacion_robot.py
```

---

## 4. Análisis de Complejidad Temporal $T(n)$

Para hallar la función de tiempo de ejecución $T(n)$, contabilizamos las operaciones elementales (asignaciones, operaciones aritméticas, comparaciones y retornos).

### A. Costo por Evaluación Individual (`determinar_orientacion`)

1. Desempaquetado de las $3$ tuplas de coordenadas (`xa, ya = a`, `xb, yb = b`, `xc, yc = c`): **$6$ operaciones** de asignación.
2. Evaluación del determinante `det = (xb - xa) * (yc - ya) - (yb - ya) * (xc - xa)`:
   - $5$ restas aritméticas.
   - $2$ multiplicaciones aritméticas.
   - $1$ asignación en memoria (`det`).
   - Subtotal: **$8$ operaciones**.
3. Estructura condicional (`if / elif / else`) y `return`:
   - **Mejor caso** ($\Delta > 0$): $1$ comparación + $1$ retorno = **$2$ operaciones**.
   - **Peor caso** ($\Delta \le 0$): $2$ comparaciones + $1$ retorno = **$3$ operaciones**.

Sumando las operaciones elementales para un único conjunto de $3$ puntos:

$$T_{\text{mejor}}(1) = 6 + 8 + 2 = 16$$

$$T_{\text{peor}}(1) = 6 + 8 + 3 = 17$$

Dado que la cantidad de instrucciones es fija y no crece con el tamaño de los datos, cada consulta de giro tiene **complejidad constante**:

$$T_{\text{consulta}} \in O(1)$$

### B. Costo Total para $n$ Casos o Tramos de Ruta: $T(n)$

Cuando el sistema de navegación procesa secuencialmente una trayectoria compuesta por $n$ tripletas de puntos:

- Inicialización del ciclo: $k = 2$ operaciones constantes.
- En cada una de las $n$ iteraciones (peor caso):
  - Control de ciclo y lectura de la tupla: $2$ operaciones.
  - Llamada a `determinar_orientacion`: $17$ operaciones.
  - Selección de acción del robot y salida: $2$ operaciones.
  - Costo por iteración: $c = 21$ operaciones elementales.

La función exacta de complejidad temporal en el peor caso es:

$$T(n) = 21n + 2$$

Aplicando notación asintótica Big $O$, el algoritmo presenta **complejidad temporal lineal**:

$$T(n) \in O(n)$$