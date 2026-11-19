from typing import Dict


def calcular_triangulacion(n: int) -> Dict[str, int]:
    """
    Calcula la cantidad de triangulos y diagonales internas necesarias
    para triangular un poligono simple de n vertices.

    Args:
        n: Numero de vertices del poligono simple (n >= 3).

    Returns:
        Diccionario con el numero de vertices, triangulos y diagonales internas.

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


def main() -> None:
    n_terreno = 5
    resultado = calcular_triangulacion(n_terreno)

    print("=== Triangulacion de Terreno Irregular ===\n")
    print(f"Vertices (n):                   {resultado['vertices']}")
    print(f"Triangulos requeridos (n - 2):  {resultado['triangulos']}")
    print(f"Diagonales internas (n - 3):    {resultado['diagonales_internas']}")


if __name__ == "__main__":
    main()