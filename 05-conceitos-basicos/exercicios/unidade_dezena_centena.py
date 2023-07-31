def main():
    print('Mostra a unidade, dezena e centena de um número.')

    # Entrada
    n: int = int(input('Digite um número inteiro positivo: '))

    # Processamento
    u: int = unidade(n)
    d: int = dezena(n)
    c: int = centena(n)

    # Saída
    print('Unidade:', u)
    print('Dezena:', d)
    print('Centena:', c)


def unidade(n: int) -> int:
    '''
    Devolve a unidade de n.

    Exemplos
    >>> unidade(152)
    2
    '''
    return n % 10


def dezena(n: int) -> int:
    '''
    Devolve a dezena de n.

    Exemplos
    >>> dezena(152)
    5
    '''
    return n // 10 % 10


def centena(n: int) -> int:
    '''
    Devolve a centena de n.

    Exemplos
    >>> centena(152)
    1
    '''
    return n // 100 % 10


if __name__ == '__main__':
    main()
