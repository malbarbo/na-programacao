def fatorial(n: int) -> int:
    '''
    Calcula o produto de todos os naturais
    entre 1 e n, isto é, 1 * ... * (n - 1) * n.
    Exemplos
    >>> fatorial(0)
    1
    >>> fatorial(1)
    1
    >>> fatorial(2)
    2
    >>> fatorial(3)
    6
    >>> fatorial(4)
    24
    '''
    fat = 1
    for i in range(2, n + 1):
        fat = fat * i
    return fat
