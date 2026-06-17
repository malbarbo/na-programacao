# Calcula estatísticas (mínima, máxima e média) das temperaturas lidas de um
# arquivo, uma temperatura por linha. O nome do arquivo é informado na linha
# de comando.
#
# Para executar:
#
#     python3 estatisticas_arquivo.py temperaturas.txt
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
    # Entrada: as temperaturas vêm das linhas do arquivo informado
    temperaturas: list[float] = []
    arquivo = open(sys.argv[1])
    for linha in arquivo:
        temperaturas.append(float(linha))
    arquivo.close()

    # Processamento e saída
    print("Mínima:", minima(temperaturas))
    print("Máxima:", maxima(temperaturas))
    print("Média:", media(temperaturas))


if __name__ == "__main__":
    main()
