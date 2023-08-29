def soma_x(lst: list[int], x: int) -> list[int]:
    '''
    Cria uma nova lista somando *x* a cada elemento de *lst*.
    Exemplos
    >>> soma_x([], 10)
    []
    >>> soma_x([3, 1, 2], 2)
    [5, 3, 4]
    '''
    lst_x = []
    for n in lst:
        lst_x.append(n + x)
    return lst_x
