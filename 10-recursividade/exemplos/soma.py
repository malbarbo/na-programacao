def soma(lst: list[int]) -> int:
    '''
    Soma os elementos de *lst*.
    Exemplos
    >>> soma([])
    0
    >>> soma([6])
    6
    >>> soma([3, 6])
    9
    >>> soma([7, 3, 6])
    16
    '''
    if lst == []:
        s = 0
    else:
        s = lst[0] + soma(lst[1:])
    return s
