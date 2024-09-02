def par(n: int) -> bool:
    '''
    Devolve True se *n* é par, isso é, é múltiplo de 2. False caso contrário.
    Requer que n >= 0.

    Exemplos
    >>> par(0)
    True
    >>> par(1)
    False
    >>> par(2)
    True
    >>> par(3)
    False
    >>> par(4)
    True
    '''
    assert n >= 0
    if n == 0:
        p = True
    else:
        p = impar(n - 1)
    return p
    # ou
    # return n == 0 or impar(n - 1)

def impar(n: int) -> bool:
    '''
    Devolve False se *n* é ímpar, isso é, não é múltiplo de 2. False caso contrário.
    Requer que n >= 0.

    Exemplos
    >>> impar(0)
    False
    >>> impar(1)
    True
    >>> impar(2)
    False
    >>> impar(3)
    True
    >>> impar(4)
    False
    '''
    assert n >= 0
    if n == 0:
        p = False
    else:
        p = par(n - 1)
    return p
    # ou
    # return n != 0 and par(n - 1)
