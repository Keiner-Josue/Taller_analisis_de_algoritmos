# Verificación de Cruce de Rutas de Autos Autónomos (Intersección de Segmentos)

Este documento desarrolla los **5 incisos** del análisis geométrico para determinar si dos trayectorias rectilíneas $\overline{ab}$ y $\overline{cd}$ de autos autónomos se cruzan, hacen contacto o se superponen en el plano cartesiano $\mathbb{R}^2$.

---

## Fundamento Matemático: Determinante de Orientación

Dada una terna ordenada de puntos $p(x_p, y_p)$, $q(x_q, y_q)$ y $r(x_r, y_r)$, su orientación en el plano se calcula mediante el determinante 2D:

$$\text{orient}(p, q, r) = \begin{vmatrix} x_q - x_p & y_q - y_p \\ x_r - x_p & y_r - y_p \end{vmatrix} = (x_q - x_p)(y_r - y_p) - (y_q - y_p)(x_r - x_p)$$

- Si $\text{orient}(p, q, r) > 0$: Giro **antihorario** (izquierda).
- Si $\text{orient}(p, q, r) < 0$: Giro **horario** (derecha).
- Si $\text{orient}(p, q, r) = 0$: Puntos **colineales**.

Para verificar si el segmento $\overline{ab}$ intersecta al segmento $\overline{cd}$, se evalúan cuatro orientaciones:

$$o_1 = \text{orient}(a, b, c), \quad o_2 = \text{orient}(a, b, d), \quad o_3 = \text{orient}(c, d, a), \quad o_4 = \text{orient}(c, d, b)$$

---

## 1. Dibujo de los Segmentos en el Plano Cartesiano

### Caso 1: $\overline{ab}$ con $a(1,1), b(7,7)$ y $\overline{cd}$ con $c(2,6), d(8,1)$

```text
  y
  7 |               b(7,7)
  6 |   c(2,6)     /
  5 |     \       /
  4 |      \     /  <-- Intersección en (4.18, 4.18)
  3 |       \   /
  2 |        \ /
  1 | a(1,1)--X-------d(8,1)
  0 +-------------------------> x
    0 1 2 3 4 5 6 7 8
```

### Caso 2: $\overline{ab}$ con $a(1,7), b(3,3)$ y $\overline{cd}$ con $c(5,5), d(7,7)$

```text
  y
  7 | a(1,7)          d(7,7)
  6 |  \             /
  5 |   \         c(5,5)
  4 |    \       .  (proyección colineal sin contacto)
  3 |     b(3,3)
  2 |
  1 |
  0 +-------------------------> x
    0 1 2 3 4 5 6 7 8
```

### Caso 3: $\overline{ab}$ con $a(0,2), b(6,2)$ y $\overline{cd}$ con $c(3,2), d(9,2)$

```text
  y
  3 |
  2 | a(0,2)======c(3,2)######b(6,2)======d(9,2)
  1 |             [Superposición]
  0 +-------------------------------------------> x
    0   1   2   3   4   5   6   7   8   9
```

---

## 2. Cálculo de las 4 Orientaciones Necesarias por Caso

### Caso 1: $a(1,1), b(7,7)$ y $c(2,6), d(8,1)$

1. $o_1 = \text{orient}(a, b, c) = (7 - 1)(6 - 1) - (7 - 1)(2 - 1) = (6)(5) - (6)(1) = 30 - 6 = +24$ (**Antihorario**)
2. $o_2 = \text{orient}(a, b, d) = (7 - 1)(1 - 1) - (7 - 1)(8 - 1) = (6)(0) - (6)(7) = 0 - 42 = -42$ (**Horario**)
3. $o_3 = \text{orient}(c, d, a) = (8 - 2)(1 - 6) - (1 - 6)(1 - 2) = (6)(-5) - (-5)(-1) = -30 - 5 = -35$ (**Horario**)
4. $o_4 = \text{orient}(c, d, b) = (8 - 2)(7 - 6) - (1 - 6)(7 - 2) = (6)(1) - (-5)(5) = 6 + 25 = +31$ (**Antihorario**)

---

### Caso 2: $a(1,7), b(3,3)$ y $c(5,5), d(7,7)$

1. $o_1 = \text{orient}(a, b, c) = (3 - 1)(5 - 7) - (3 - 7)(5 - 1) = (2)(-2) - (-4)(4) = -4 + 16 = +12$ (**Antihorario**)
2. $o_2 = \text{orient}(a, b, d) = (3 - 1)(7 - 7) - (3 - 7)(7 - 1) = (2)(0) - (-4)(6) = 0 + 24 = +24$ (**Antihorario**)
3. $o_3 = \text{orient}(c, d, a) = (7 - 5)(7 - 5) - (7 - 5)(1 - 5) = (2)(2) - (2)(-4) = 4 + 8 = +12$ (**Antihorario**)
4. $o_4 = \text{orient}(c, d, b) = (7 - 5)(3 - 5) - (7 - 5)(3 - 5) = (2)(-2) - (2)(-2) = -4 + 4 = 0$ (**Colineal**)

---

### Caso 3: $a(0,2), b(6,2)$ y $c(3,2), d(9,2)$

1. $o_1 = \text{orient}(a, b, c) = (6 - 0)(2 - 2) - (2 - 2)(3 - 0) = (6)(0) - (0)(3) = 0$ (**Colineal**)
2. $o_2 = \text{orient}(a, b, d) = (6 - 0)(2 - 2) - (2 - 2)(9 - 0) = (6)(0) - (0)(9) = 0$ (**Colineal**)
3. $o_3 = \text{orient}(c, d, a) = (9 - 3)(2 - 2) - (2 - 2)(0 - 3) = (6)(0) - (0)(-3) = 0$ (**Colineal**)
4. $o_4 = \text{orient}(c, d, b) = (9 - 3)(2 - 2) - (2 - 2)(6 - 3) = (6)(0) - (0)(3) = 0$ (**Colineal**)

---

## 3. Determinación de Intersección (Cruces, Contactos y Superposiciones)

### Criterios de Evaluación

1. **Caso general (cruce propio):** Existe intersección si y solo si los puntos de cada segmento quedan en semiplanos opuestos respecto al otro:
   $$(o_1 \cdot o_2 < 0) \land (o_3 \cdot o_4 < 0)$$
2. **Casos especiales (colinealidad, contacto en extremo o superposición):** Si alguna orientación $o_i = 0$, se verifica mediante proyección sobre los ejes (*bounding box*) si el punto colineal pertenece al intervalo cerrado del segmento opuesto:
   $$\min(x_p, x_r) \le x_q \le \max(x_p, x_r) \quad \land \quad \min(y_p, y_r) \le y_q \le \max(y_p, y_r)$$

### Diagnóstico por Caso

- **Caso 1:** **SÍ existe intersección propia (cruce en X).** Se cumple que $o_1 = +24 > 0$ y $o_2 = -42 < 0$ (signos opuestos), y simultáneamente $o_3 = -35 < 0$ y $o_4 = +31 > 0$ (signos opuestos). Las rutas se cruzan en el punto exacto $\left(\frac{46}{11}, \frac{46}{11}\right) \approx (4.18, 4.18)$.
- **Caso 2:** **NO existe intersección.** Aunque $o_4 = 0$ indica que $b(3,3)$ es colineal con la recta infinita que contiene a $\overline{cd}$ ($y = x$), al verificar el rango del segmento $\overline{cd}$ ($x \in [5, 7], y \in [5, 7]$), se observa que $3 \notin [5, 7]$. Además, $o_1$ y $o_2$ tienen el mismo signo ($+12$ y $+24$). Los segmentos son completamente disjuntos.
- **Caso 3:** **SÍ existe intersección por superposición colineal.** Todas las orientaciones son $0$ (los cuatro puntos yacen sobre la recta $y = 2$) y los intervalos se solapan: $c(3,2)$ cae dentro de $\overline{ab}$ ($0 \le 3 \le 6$) y $b(6,2)$ cae dentro de $\overline{cd}$ ($3 \le 6 \le 9$). Ambos segmentos comparten el tramo desde $(3,2)$ hasta $(6,2)$.

### Tabla Resumen de Resultados

| Caso | $o_1(a,b,c)$ | $o_2(a,b,d)$ | $o_3(c,d,a)$ | $o_4(c,d,b)$ | ¿Existe Intersección? | Tipo de Intersección |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Caso 1** | $+24$ | $-42$ | $-35$ | $+31$ | **Sí** | Intersección propia en $\left(\frac{46}{11}, \frac{46}{11}\right)$ |
| **Caso 2** | $+12$ | $+24$ | $+12$ | $0$ | **No** | Disjuntos ($b$ colineal fuera de $\overline{cd}$) |
| **Caso 3** | $0$ | $0$ | $0$ | $0$ | **Sí** | Superposición colineal en tramo $(3,2) - (6,2)$ |

---

## 4. Función en Python con 4 Parámetros

La implementación completa se encuentra en el archivo `interseccion_segmentos.py`:

```python
from typing import Tuple

Punto = Tuple[float, float]


def orientacion(p: Punto, q: Punto, r: Punto) -> float:
    """Calcula el determinante de orientacion 2D para (p, q, r)."""
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])


def en_segmento(p: Punto, q: Punto, r: Punto) -> bool:
    """Verifica si el punto q pertenece al segmento pr (asumiendo colinealidad)."""
    return (
        min(p[0], r[0]) <= q[0] <= max(p[0], r[0])
        and min(p[1], r[1]) <= q[1] <= max(p[1], r[1])
    )


def interseccion_segmentos(a: Punto, b: Punto, c: Punto, d: Punto) -> bool:
    """
    Recibe 4 parametros (puntos extremos a, b del primer segmento y c, d del segundo)
    y determina si existe interseccion, incluyendo contactos y superposiciones.
    """
    o1 = orientacion(a, b, c)
    o2 = orientacion(a, b, d)
    o3 = orientacion(c, d, a)
    o4 = orientacion(c, d, b)

    # 1. Caso general: cruce propio
    if ((o1 > 0 and o2 < 0) or (o1 < 0 and o2 > 0)) and (
        (o3 > 0 and o4 < 0) or (o3 < 0 and o4 > 0)
    ):
        return True

    # 2. Casos especiales: colinealidad, contacto en extremo o superposicion
    if o1 == 0 and en_segmento(a, c, b):
        return True
    if o2 == 0 and en_segmento(a, d, b):
        return True
    if o3 == 0 and en_segmento(c, a, d):
        return True
    if o4 == 0 and en_segmento(c, b, d):
        return True

    return False
```

### Ejecución

```bash
python interseccion_segmentos.py
```

---

## 5. ¿Por qué la Intersección de Dos Segmentos Tiene Complejidad $O(1)$?

La verificación de intersección entre dos segmentos de recta individuales posee **complejidad temporal y espacial constante $O(1)$** por tres razones fundamentales:

1. **Entrada de tamaño fijo y acotado:** El algoritmo recibe siempre exactamente **4 puntos** ($8$ coordenadas escalares). No procesa arreglos ni listas dinámicas de $n$ elementos.
2. **Ausencia de ciclos y recursión:** El flujo de ejecución es puramente secuencial y ramificado mediante condicionales simples. En cualquier ejecución se calculan exactamente **4 determinantes de orientación** (cada uno requiere $5$ restas y $2$ multiplicaciones) y, en el peor escenario (colinealidad), se evalúan hasta **4 comprobaciones de rango** (`en_segmento`) con comparaciones elementales de mínimo y máximo.
3. **Costo operacional constante:** Sin importar la longitud física de las rutas ni la magnitud de sus coordenadas en el plano, la cantidad máxima de operaciones elementales de CPU es una cota constante ($T(n) = c \le 60$ instrucciones), lo que por definición asintótica corresponde a $O(1)$.