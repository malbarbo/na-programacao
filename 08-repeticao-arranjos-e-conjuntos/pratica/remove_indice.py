def remove_indice(lst: list[int], i: int) -> list[int]:
    '''
    Produz uma nova lista removendo o elemento que está na posição *i* de *lst*.
    Requer que 0 <= i < len(lst).
    Exemplos
    >>> remove_indice([3], 0)
    []
    >>> remove_indice([3, 5, 1], 0)
    [5, 1]
    >>> remove_indice([3, 5, 1], 1)
    [3, 1]
    >>> remove_indice([3, 5, 1], 2)
    [3, 5]
    '''
    assert 0 <= i < len(lst)

    # Adiciona os anteriores a i
    sem_i = []
    for j in range(i):
        sem_i.append(lst[j])

    # Adiciona os posteriores a i
    for j in range(i + 1, len(lst)):
        sem_i.append(lst[j])

    return sem_i
