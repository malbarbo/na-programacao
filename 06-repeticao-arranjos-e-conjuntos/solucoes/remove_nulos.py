def remove_nulos(lst: list[int]) -> list[int]:
    '''
    Produz uma nova lista removendo todos os valores nulos (0) de *lst*.
    Exemplos
    >>> remove_nulos([])
    []
    >>> remove_nulos([4, 1, 0, 3, 0])
    [4, 1, 3]
    '''
    sem_nulos = []
    for n in lst:
        if n != 0:
            sem_nulos.append(n)
    return sem_nulos
