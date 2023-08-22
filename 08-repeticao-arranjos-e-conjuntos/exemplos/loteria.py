from dataclasses import dataclass

# Análise
#
# Determinar se um número está entre 6 números sorteados.
# Determinar o número de acertos de uma aposta de 6 números sendo que 6 números foram sorteados;
# Os números estão entre 1 e 60;

# Definição de tipos de dados
#
# A aposta e os sorteados, são composta de seis número, então vamos usar lista de inteiros.

def numero_acertos(aposta: list[int], sorteados: list[int]) -> int:
    '''
    Determina quantos números da *aposta* estão em *sorteados*.

    Exemplos
    >>> numero_acertos([1, 2, 3, 4, 5, 6], [8, 12, 20, 41, 52, 57])
    0
    >>> numero_acertos([8, 2, 3, 4, 5, 6], [8, 12, 20, 41, 52, 57])
    1
    >>> numero_acertos([8, 12, 3, 4, 5, 6], [8, 12, 20, 41, 52, 57])
    2
    >>> numero_acertos([8, 12, 20, 4, 5, 6], [8, 12, 20, 41, 52, 57])
    3
    >>> numero_acertos([8, 12, 20, 41, 5, 6], [8, 12, 20, 41, 52, 57])
    4
    >>> numero_acertos([8, 12, 20, 41, 52, 6], [8, 12, 20, 41, 52, 57])
    5
    >>> numero_acertos([8, 12, 20, 41, 52, 57], [8, 12, 20, 41, 52, 57])
    6
    '''
    acertos = 0

    for n in aposta:
       if sorteado(n, sorteados):
           acertos = acertos + 1

    return acertos


def sorteado(n: int, sorteados: list[int]) -> bool:
    '''
    Produz True se *n* é um dos números em *sorteados*. False caso contrário.

    Exemplos
    >>> sorteados = [1, 7, 10, 40, 41, 60]
    >>> sorteado(1, sorteados)
    True
    >>> sorteado(7, sorteados)
    True
    >>> sorteado(10, sorteados)
    True
    >>> sorteado(40, sorteados)
    True
    >>> sorteado(41, sorteados)
    True
    >>> sorteado(60, sorteados)
    True
    >>> sorteado(2, sorteados)
    False
    '''
    em_sorteados = False

    for x in sorteados:
        if n == x:
            em_sorteados = True

    return em_sorteados
