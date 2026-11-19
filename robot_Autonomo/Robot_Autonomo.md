# Navegación de Robot Autónomo mediante Geometría Computacional

Este repositorio contiene el análisis matemático, la implementación en Python y el estudio de complejidad algorítmica $T(n)$ para determinar la dirección de giro de un robot autónomo en una bodega a partir de tres puntos en el plano cartesiano 2D.

---

## 1. Fundamentación Matemática y Cálculo de Determinantes

En geometría computacional, dada una secuencia ordenada de tres puntos en el plano $\mathbb{R}^2$:

- $A(x_1, y_1)$: Posición anterior del robot.
- $B(x_2, y_2)$: Posición actual del robot.
- $C(x_3, y_3)$: Posición de destino.

La orientación del trayecto $A \to B \to C$ se determina mediante el **producto cruz en 2D** (equivalente al determinante de orientación) formado por los vectores $\vec{AB} = (x_2 - x_1, y_2 - y_1)$ y $\vec{AC} = (x_3 - x_1, y_3 - y_1)$:

$$\Delta = \det(A, B, C) = \begin{vmatrix} x_2 - x_1 & y_2 - y_1 \\ x_3 - x_1 & y_3 - y_1 \end{vmatrix} = (x_2 - x_1)(y_3 - y_1) - (y_2 - y_1)(x_3 - x_1)$$

De forma equivalente, mediante coordenadas homogéneas en una matriz de $3 \times 3$:

$$\Delta = \begin{vmatrix} x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \\ x_3 & y_3 & 1 \end{vmatrix}$$

### Criterio de Clasificación Geométrica (Regla de la Mano Derecha)

- Si $\Delta > 0$: El robot gira hacia la izquierda (**Giro antihorario**).
- Si $\Delta < 0$: El robot gira hacia la derecha (**Giro horario**).
- Si $\Delta = 0$: Los tres puntos están alineados sobre la misma recta (**Colineal**, avanza sin girar).

---

### Desarrollo Paso a Paso por Caso

#### **Caso 1:** $A(1, 2)$, $B(5, 3)$, $C(3, 7)$

1. Vectores respecto a $A$:
   $$\vec{AB} = (5 - 1, 3 - 2) = (4, 1)$$
   $$\vec{AC} = (3 - 1, 7 - 2) = (2, 5)$$
2. Cálculo del determinante:
   $$\Delta_1 = (4)(5) - (1)(2) = 20 - 2 = 18$$
3. Clasificación: Como $\Delta_1 = 18 > 0$, corresponde a un **Giro antihorario**.

---

#### **Caso 2:** $A(2, 1)$, $B(6, 5)$, $C(8, 2)$

1. Vectores respecto a $A$:
   $$\vec{AB} = (6 - 2, 5 - 1) = (4, 4)$$
   $$\vec{AC} = (8 - 2, 2 - 1) = (6, 1)$$
2. Cálculo del determinante:
   $$\Delta_2 = (4)(1) - (4)(6) = 4 - 24 = -20$$
3. Clasificación: Como $\Delta_2 = -20 < 0$, corresponde a un **Giro horario**.

---

#### **Caso 3:** $A(1, 1)$, $B(3, 3)$, $C(6, 6)$

1. Vectores respecto a $A$:
   $$\vec{AB} = (3 - 1, 3 - 1) = (2, 2)$$
   $$\vec{AC} = (6 - 1, 6 - 1) = (5, 5)$$
2. Cálculo del determinante:
   $$\Delta_3 = (2)(5) - (2)(5) = 10 - 10 = 0$$
3. Clasificación: Como $\Delta_3 = 0$, los puntos son **Colineales**.

---

#### **Caso 4:** $A(0, 4)$, $B(5, 4)$, $C(3, 1)$

1. Vectores respecto a $A$:
   $$\vec{AB} = (5 - 0, 4 - 4) = (5, 0)$$
   $$\vec{AC} = (3 - 0, 1 - 4) = (3, -3)$$
2. Cálculo del determinante:
   $$\Delta_4 = (5)(-3) - (0)(3) = -15 - 0 = -15$$
3. Clasificación: Como $\Delta_4 = -15 < 0$, corresponde a un **Giro horario**.

---

### Tabla Resumen de Resultados

| Caso | Punto $A$ (Anterior) | Punto $B$ (Actual) | Punto $C$ (Destino) | Determinante ($\Delta$) | Clasificación de Giro |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **Caso 1** | $(1, 2)$ | $(5, 3)$ | $(3, 7)$ | $18$ | Giro antihorario |
| **Caso 2** | $(2, 1)$ | $(6, 5)$ | $(8, 2)$ | $-20$ | Giro horario |
| **Caso 3** | $(1, 1)$ | $(3, 3)$ | $(6, 6)$ | $0$ | Colineal |
| **Caso 4** | $(0, 4)$ | $(5, 4)$ | $(3, 1)$ | $-15$ | Giro horario |

---

## 2. Implementación en Python

El algoritmo se encuentra implementado en el archivo `orientacion_robot.py`:

```python
from typing import Tuple


def calcular_orientacion(
    a: Tuple[float, float],
    b: Tuple[float, float],
    c: Tuple[float, float]
) -> Tuple[float, str]:
    """
    Calcula el determinante de orientacion 2D para tres puntos A, B y C
    y clasifica el giro del robot autonomo.
    """
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    determinante = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

    if determinante > 0:
        clasificacion = "Giro antihorario"
    elif determinante < 0:
        clasificacion = "Giro horario"
    else:
        clasificacion = "Colineal"

    return determinante, clasificacion


if __name__ == "__main__":
    casos = [
        ("Caso 1", (1, 2), (5, 3), (3, 7)),
        ("Caso 2", (2, 1), (6, 5), (8, 2)),
        ("Caso 3", (1, 1), (3, 3), (6, 6)),
        ("Caso 4", (0, 4), (5, 4), (3, 1)),
    ]

    for nombre, a, b, c in casos:
        det, giro = calcular_orientacion(a, b, c)
        print(f"{nombre}: A{a}, B{b}, C{c} -> Determinante = {det} | {giro}")
```

### Ejecución

```bash
python orientacion_robot.py
```

---

## 3. Análisis de Complejidad Temporal $T(n)$

Para determinar la eficiencia computacional del sistema de navegación del robot, se contabilizan las operaciones elementales (asignaciones, operaciones aritméticas, comparaciones y retornos).

### A. Costo por Evaluación Individual (`calcular_orientacion`)

Desglosando línea por línea la función para un triplete de puntos $(A, B, C)$:

1. Desempaquetado de coordenadas (`x1, y1 = a`, `x2, y2 = b`, `x3, y3 = c`): **$6$ operaciones** de asignación.
2. Cálculo del determinante `(x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)`:
   - $5$ restas aritméticas.
   - $2$ multiplicaciones aritméticas.
   - $1$ asignación a la variable `determinante`.
   - Total en esta instrucción: **$8$ operaciones**.
3. Estructura condicional (`if / elif / else`) y asignación de resultado:
   - **Mejor caso** ($\Delta > 0$): $1$ comparación + $1$ asignación = **$2$ operaciones**.
   - **Peor caso** ($\Delta \le 0$): $2$ comparaciones + $1$ asignación = **$3$ operaciones**.
4. Instrucción `return`: **$1$ operación**.

Sumando las operaciones elementales para un único caso:

$$T_{\text{mejor}}(1) = 6 + 8 + 2 + 1 = 17$$

$$T_{\text{peor}}(1) = 6 + 8 + 3 + 1 = 18$$

Dado que el número de operaciones no depende del tamaño de entrada, evaluar un giro individual tiene **complejidad constante**:

$$T_{\text{caso}} \in O(1)$$

### B. Costo Total para $n$ Casos de Prueba: $T(n)$

Si el algoritmo procesa una lista de $n$ conjuntos de puntos mediante un ciclo iterativo:

- Inicialización del ciclo y estructuras de control: $k = 2$ operaciones constantes.
- En cada una de las $n$ iteraciones (peor caso):
  - Control de iteración y acceso a la tupla: $2$ operaciones.
  - Ejecución de `calcular_orientacion`: $18$ operaciones.
  - Formateo e impresión de salida: $1$ operación.
  - Total por iteración: $c = 21$ operaciones elementales.

Por lo tanto, la función exacta de tiempo de ejecución en el peor caso es:

$$T(n) = 21n + 2$$

Aplicando análisis asintótico (descartando constantes multiplicativas y términos de menor orden), la complejidad temporal del algoritmo es **lineal**:

$$T(n) \in O(n)$$

### C. Complejidad Espacial $S(n)$

- **Por consulta en tiempo real (streaming del robot):** $S(1) \in O(1)$, ya que solo se almacenan variables escalares temporales en memoria.
- **Para un lote almacenado de $n$ casos:** $S(n) \in O(n)$, proporcional a la cantidad de coordenadas guardadas en la lista de entrada.