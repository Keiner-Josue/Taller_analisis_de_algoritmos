from typing import Tuple

Punto = Tuple[float, float]


def orientacion(p: Punto, q: Punto, r: Punto) -> float:
    """
    Calcula el determinante de orientacion 2D para la terna ordenada (p, q, r):
    det = (xq - xp)(yr - yp) - (yq - yp)(xr - xp)
    """
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])


def en_segmento(p: Punto, q: Punto, r: Punto) -> bool:
    """
    Verifica si el punto colineal q yace sobre el segmento cerrado pr
    comprobando su pertenencia al rectangulo delimitador (bounding box).
    """
    return (
        min(p[0], r[0]) <= q[0] <= max(p[0], r[0])
        and min(p[1], r[1]) <= q[1] <= max(p[1], r[1])
    )


def interseccion_segmentos(a: Punto, b: Punto, c: Punto, d: Punto) -> bool:
    """
    Determina si los segmentos ab y cd se intersectan, incluyendo cruces propios,
    contactos en extremos y superposiciones colineales.

    Args:
        a: Punto inicial del primer segmento.
        b: Punto final del primer segmento.
        c: Punto inicial del segundo segmento.
        d: Punto final del segundo segmento.

    Returns:
        True si existe algun tipo de interseccion; False en caso contrario.

    Complejidad temporal: O(1)
    Complejidad espacial: O(1)
    """
    o1 = orientacion(a, b, c)
    o2 = orientacion(a, b, d)
    o3 = orientacion(c, d, a)
    o4 = orientacion(c, d, b)

    # 1. Caso general: cruce propio en X
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


def main() -> None:
    casos = [
        ("Caso 1", (1, 1), (7, 7), (2, 6), (8, 1)),
        ("Caso 2", (1, 7), (3, 3), (5, 5), (7, 7)),
        ("Caso 3", (0, 2), (6, 2), (3, 2), (9, 2)),
    ]

    print("=== Verificacion de Cruce de Rutas (Autos Autonomos) ===\n")
    for nombre, a, b, c, d in casos:
        o1 = orientacion(a, b, c)
        o2 = orientacion(a, b, d)
        o3 = orientacion(c, d, a)
        o4 = orientacion(c, d, b)
        hay_cruce = interseccion_segmentos(a, b, c, d)

        print(f"{nombre}: ab=[{a}, {b}], cd=[{c}, {d}]")
        print(f"  Orientaciones -> o1={o1}, o2={o2}, o3={o3}, o4={o4}")
        print(f"  ¿Existe interseccion?: {'SI' if hay_cruce else 'NO'}\n")


if __name__ == "__main__":
    main()