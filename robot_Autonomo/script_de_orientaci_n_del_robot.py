from typing import Tuple


def calcular_orientacion(
    a: Tuple[float, float],
    b: Tuple[float, float],
    c: Tuple[float, float]
) -> Tuple[float, str]:
    """
    Calcula el determinante de orientacion 2D para tres puntos A, B y C
    y clasifica el giro del robot autonomo.

    Args:
        a: Coordenadas (x1, y1) de la posicion anterior.
        b: Coordenadas (x2, y2) de la posicion actual.
        c: Coordenadas (x3, y3) de la posicion de destino.

    Returns:
        Una tupla con el valor del determinante y su clasificacion geometrica.
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


def main() -> None:
    casos = [
        ("Caso 1", (1, 2), (5, 3), (3, 7)),
        ("Caso 2", (2, 1), (6, 5), (8, 2)),
        ("Caso 3", (1, 1), (3, 3), (6, 6)),
        ("Caso 4", (0, 4), (5, 4), (3, 1)),
    ]

    print("=== Clasificacion de Orientacion del Robot Autonomo ===\n")
    for nombre, a, b, c in casos:
        det, giro = calcular_orientacion(a, b, c)
        print(f"{nombre}: A{a}, B{b}, C{c} -> Determinante = {det:>4} | {giro}")


if __name__ == "__main__":
    main()