def maximo(lst: list[int]) -> int:
    '''
    Encontra o valor máximo de *lst*.
    Requer que lst seja não vazia.
    Exemplos
    >>> maximo([7])
    7
    >>> maximo([-1, -4, 0])
    0
    '''
    assert len(lst) != 0
    maximo = lst[0]
    for n in lst:
        if n > maximo:
            maximo = n
    return n
