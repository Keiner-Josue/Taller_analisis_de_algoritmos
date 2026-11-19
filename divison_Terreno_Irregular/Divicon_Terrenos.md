# Triangulación de Terreno Irregular mediante Geometría Computacional

Este documento contiene el análisis geométrico, la clasificación de vértices por orientación, el estudio del algoritmo *Ear Clipping* (recorte de orejas) y la implementación en Python para particionar un terreno poligonal simple en regiones triangulares.

---

## Datos del Terreno

El polígono simple está definido por $n = 5$ vértices conectados secuencialmente:

$$A(0,0) \to B(8,0) \to C(8,6) \to D(4,3) \to E(0,6) \to A(0,0)$$

---

## 1. Identificación de Vértices Convexos y Cóncavos

### Verificación del Sentido de Recorrido

Antes de evaluar los determinantes locales, determinamos la orientación global del polígono mediante la fórmula del área con signo (fórmula de la lazada):

$$2\mathcal{A} = \sum_{i=1}^{n} (x_i y_{i+1} - x_{i+1} y_i)$$

Sustituyendo las coordenadas en orden $A \to B \to C \to D \to E \to A$:

$$2\mathcal{A} = (0 \cdot 0 - 8 \cdot 0) + (8 \cdot 6 - 8 \cdot 0) + (8 \cdot 3 - 4 \cdot 6) + (4 \cdot 6 - 0 \cdot 3) + (0 \cdot 0 - 0 \cdot 6)$$

$$2\mathcal{A} = 0 + 48 + 0 + 24 + 0 = 72 \implies \mathcal{A} = 36\text{ u}^2 > 0$$

Como el área con signo es positiva, los vértices están ordenados en **sentido antihorario (CCW)**.

### Criterio del Determinante de Orientación

Para cada terna de vértices consecutivos $(V_{i-1}, V_i, V_{i+1})$ en un polígono recorrido en sentido antihorario, se evalúa:

$$\det(V_{i-1}, V_i, V_{i+1}) = \begin{vmatrix} x_i - x_{i-1} & y_i - y_{i-1} \\ x_{i+1} - x_{i-1} & y_{i+1} - y_{i-1} \end{vmatrix} = (x_i - x_{i-1})(y_{i+1} - y_{i-1}) - (y_i - y_{i-1})(x_{i+1} - x_{i-1})$$

- Si $\det > 0$: Giro a la izquierda (antihorario), ángulo interior $< 180^\circ \implies$ **Vértice convexo**.
- Si $\det < 0$: Giro a la derecha (horario), ángulo interior $> 180^\circ \implies$ **Vértice cóncavo (reflejo)**.

### Cálculo Paso a Paso por Vértice

1. **Vértice $A(0,0)$** con terna $(E \to A \to B)$:
   $$\det(E, A, B) = (0 - 0)(0 - 6) - (0 - 6)(8 - 0) = 0 - (-48) = +48 > 0$$

2. **Vértice $B(8,0)$** con terna $(A \to B \to C)$:
   $$\det(A, B, C) = (8 - 0)(6 - 0) - (0 - 0)(8 - 0) = 48 - 0 = +48 > 0$$

3. **Vértice $C(8,6)$** con terna $(B \to C \to D)$:
   $$\det(B, C, D) = (8 - 8)(3 - 0) - (6 - 0)(4 - 8) = 0 - (-24) = +24 > 0$$

4. **Vértice $D(4,3)$** con terna $(C \to D \to E)$:
   $$\det(C, D, E) = (4 - 8)(6 - 6) - (3 - 6)(0 - 8) = 0 - 24 = -24 < 0$$

5. **Vértice $E(0,6)$** con terna $(D \to E \to A)$:
   $$\det(D, E, A) = (0 - 4)(0 - 3) - (6 - 3)(0 - 4) = 12 - (-12) = +24 > 0$$

### Tabla Resumen de Vértices

| Vértice | Coordenadas | Terna Evaluada | Determinante | Tipo de Giro | Clasificación |
| :---: | :---: | :---: | :---: | :--- | :--- |
| **$A$** | $(0,0)$ | $E \to A \to B$ | $+48$ | Antihorario | **Convexo** |
| **$B$** | $(8,0)$ | $A \to B \to C$ | $+48$ | Antihorario | **Convexo** |
| **$C$** | $(8,6)$ | $B \to C \to D$ | $+24$ | Antihorario | **Convexo** |
| **$D$** | $(4,3)$ | $C \to D \to E$ | $-24$ | Horario | **Cóncavo (reflejo)** |
| **$E$** | $(0,6)$ | $D \to E \to A$ | $+24$ | Antihorario | **Convexo** |

---

## 2. Cantidad de Triángulos y Diagonales Internas

Para todo polígono simple de $n$ vértices (con $n = 5$):

- **Número de triángulos ($T$):**
  $$T = n - 2 = 5 - 2 = 3\text{ triángulos}$$

- **Número de diagonales internas ($D$):**
  $$D = n - 3 = 5 - 3 = 2\text{ diagonales internas}$$

---

## 3. Representación de una Triangulación Válida

En este polígono, el vértice cóncavo $D(4,3)$ coincide exactamente con el punto medio de los segmentos $\overline{AC}$ y $\overline{EB}$, por lo que dichos segmentos tocan el borde interior del terreno y no son diagonales estrictamente internas.

La triangulación válida utiliza las **2 diagonales internas $\overline{BD}$ y $\overline{DA}$**, dividiendo el terreno en los **3 triángulos no degenerados**:

- $T_1 = \triangle BCD$ (Área $= 12\text{ u}^2$)
- $T_2 = \triangle DEA$ (Área $= 12\text{ u}^2$)
- $T_3 = \triangle ABD$ (Área $= 12\text{ u}^2$)

```text
  y
  6 | E(0,6)                         C(8,6)
    | * .                         . *
    | |   .                     .   |
    | |     .     (Exterior)  .     |
  3 | |       .     D(4,3)  .       |
    | |  T2     .     *   .     T1  |
    | |           . /   \ .         |
    | |          . /     \ .        |
    | |         . /  T3   \ .       |
  0 | *----------*---------*--------*-----> x
    0 A(0,0)     2         4      8 B(8,0)

  Bordes del terreno (-): A-B, B-C, C-D, D-E, E-A
  Diagonales internas (/ y \): D-A y B-D
```

---

## 4. Primera Oreja Recortable mediante Ear Clipping

En el algoritmo *Ear Clipping*, una **oreja** es un triángulo formado por tres vértices consecutivos $\triangle V_{i-1} V_i V_{i+1}$ tal que $V_i$ es estrictamente convexo y ningún otro vértice del polígono cae en su interior ni sobre sus bordes.

- **Descarte de $A$ y $B$:** Aunque son convexos ($\det = +48$), el vértice cóncavo $D(4,3)$ cae exactamente sobre la diagonal de cierre $\overline{EB}$ en $\triangle EAB$ y sobre $\overline{AC}$ en $\triangle ABC$, invalidando ambos candidatos.
- **Primera oreja válida:** Al recorrer los vértices en orden, el **vértice $C$** (que forma el triángulo **$\triangle BCD$**) es la **primera oreja válida** (de forma análoga, el vértice $E$ con $\triangle DEA$ también cumple todas las condiciones desde el inicio):
  1. $C$ es estrictamente convexo ($\det(B, C, D) = +24 > 0$).
  2. Los vértices restantes $A(0,0)$ y $E(0,6)$ tienen coordenada $x = 0$, quedando completamente fuera de $\triangle BCD$ (cuyo intervalo en $x$ es $[4, 8]$).
  3. Al recortar $C$, se traza la primera diagonal interna **$\overline{BD}$** y el polígono se reduce al cuadrilátero $A - B - D - E$.

---

## 5. Condiciones a Verificar antes de Retirar un Vértice

Antes de recortar un vértice candidato $V_i$ (con triángulo asociado $\triangle V_{i-1} V_i V_{i+1}$) durante el proceso de *Ear Clipping*, se deben validar tres condiciones fundamentales:

1. **Cardinalidad mínima del polígono ($n > 3$):** El polígono activo debe conservar al menos 4 vértices. Cuando $n = 3$, el polígono restante ya es el último triángulo de la partición y el algoritmo finaliza.
2. **Convexidad estricta del vértice $V_i$:** El determinante de orientación $\det(V_{i-1}, V_i, V_{i+1})$ debe tener el mismo signo que el recorrido global del polígono ($\det > 0$ en sentido antihorario, ángulo interior $< 180^\circ$). Si $\det \le 0$, el vértice es cóncavo o colineal y su triángulo quedaría fuera del terreno o sería degenerado.
3. **Ausencia de otros vértices dentro o sobre el borde del triángulo:** Ningún otro vértice $V_k \notin \{V_{i-1}, V_i, V_{i+1}\}$ (en la práctica basta comprobar los vértices cóncavos/reflejos) puede ubicarse en el interior estricto ni sobre los lados de $\triangle V_{i-1} V_i V_{i+1}$ (especialmente sobre la nueva diagonal $\overline{V_{i-1}V_{i+1}}$). Esto asegura que la diagonal sea puramente interna y no corte ninguna arista del terreno.

---

## 6. Implementación en Python

El código se encuentra disponible en `triangulacion_poligono.py`:

```python
from typing import Dict


def calcular_triangulacion(n: int) -> Dict[str, int]:
    """
    Calcula la cantidad de triangulos y diagonales internas necesarias
    para triangular un poligono simple de n vertices.

    Complejidad temporal: O(1)
    Complejidad espacial: O(1)
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("El numero de vertices 'n' debe ser un entero.")
    if n < 3:
        raise ValueError("Un poligono requiere al menos n = 3 vertices.")

    triangulos = n - 2
    diagonales_internas = n - 3

    return {
        "vertices": n,
        "triangulos": triangulos,
        "diagonales_internas": diagonales_internas,
    }


if __name__ == "__main__":
    resultado = calcular_triangulacion(5)
    print(f"Vertices (n): {resultado['vertices']}")
    print(f"Triangulos requeridos: {resultado['triangulos']}")
    print(f"Diagonales internas requeridas: {resultado['diagonales_internas']}")
```

### Ejecución

```bash
python triangulacion_poligono.py
```