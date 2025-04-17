def dobrada(lst: list[int]) -> bool:
    '''
    Produz True se *lst* é dobrada, isto é, pode
    ser obtida pela concatenação de duas listas iguais.
    Devolve False caso contrário.

    Exemplos
    >>> dobrada([])
    True
    >>> dobrada([3])
    False
    >>> dobrada([3, 3])
    True
    >>> dobrada([3, 2])
    False
    >>> dobrada([2, 6, 1, 2, 6, 1])
    True
    >>> dobrada([2, 6, 1, 2, 6, 1, 4])
    False
    '''
    dobrada = len(lst) % 2 == 0
    meio = len(lst) // 2
    i = 0
    while i < meio and dobrada:
        if lst[i] != lst[meio + i]:
            dobrada = False
        i = i + 1
    return dobrada
