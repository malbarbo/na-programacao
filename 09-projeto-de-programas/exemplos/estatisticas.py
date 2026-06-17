# Calcula estatísticas (mínima, máxima e média) de uma lista de temperaturas
# informadas na linha de comando.
#
# Para executar:
#
#     python3 estatisticas.py 20.5 19.0 22.0 25.5
#
# Este programa não valida a entrada.

import sys


def minima(temperaturas: list[float]) -> float:
    """
    Devolve a menor temperatura de *temperaturas*.
    Requer que *temperaturas* seja não vazia.

    >>> minima([20.5])
    20.5
    >>> minima([20.5, 19.0, 22.0, 25.5])
    19.0
    """
    menor: float = temperaturas[0]
    for t in temperaturas:
        if t < menor:
            menor = t
    return menor


def maxima(temperaturas: list[float]) -> float:
    """
    Devolve a maior temperatura de *temperaturas*.
    Requer que *temperaturas* seja não vazia.

    >>> maxima([20.5])
    20.5
    >>> maxima([20.5, 19.0, 22.0, 25.5])
    25.5
    """
    maior: float = temperaturas[0]
    for t in temperaturas:
        if t > maior:
            maior = t
    return maior


def media(temperaturas: list[float]) -> float:
    """
    Devolve a média aritmética de *temperaturas*.
    Requer que *temperaturas* seja não vazia.

    >>> media([20.0])
    20.0
    >>> media([20.5, 19.0, 22.0])
    20.5
    """
    soma: float = 0.0
    for t in temperaturas:
        soma += t
    return soma / len(temperaturas)


def main() -> None:
    # Entrada: as temperaturas vêm dos argumentos da linha de comando
    temperaturas: list[float] = []
    for argumento in sys.argv[1:]:
        temperaturas.append(float(argumento))

    # Processamento e saída
    print("Mínima:", minima(temperaturas))
    print("Máxima:", maxima(temperaturas))
    print("Média:", media(temperaturas))


if __name__ == "__main__":
    main()
