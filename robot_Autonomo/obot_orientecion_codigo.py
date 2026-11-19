from typing import Tuple


def determinar_orientacion(
    a: Tuple[float, float],
    b: Tuple[float, float],
    c: Tuple[float, float],
) -> str:
    """
    Calcula el determinante (xb - xa)(yc - ya) - (yb - ya)(xc - xa)
    para tres puntos en el plano 2D y retorna su orientacion:
    'Antihorario', 'Horario' o 'Colineal'.
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
    Determina hacia donde debe girar el robot autonomo a partir de
    su posicion actual (a), objetivo (b) y destino (c).

    Returns:
        Tupla con (valor_determinante, orientacion, decision_de_giro).
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


def main() -> None:
    casos = [
        ("Caso 1", (4, 2), (5, 3), (3, 7)),
        ("Caso 2", (2, 7), (6, 5), (8, 2)),
        ("Caso 3", (1, 7), (3, 3), (6, 6)),
        ("Caso 4", (0, 4), (5, 4), (3, 1)),
    ]

    print("=== Sistema de Decision de Giro del Robot Autonomo ===\n")
    for nombre, a, b, c in casos:
        det, orientacion, decision = decidir_giro_robot(a, b, c)
        print(
            f"{nombre}: a{a}, b{b}, c{c} | "
            f"det = {det:>4} | Orientacion: {orientacion:<11} | Decision: {decision}"
        )


if __name__ == "__main__":
    main()