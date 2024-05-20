def algum_true(lst: list[bool]) -> bool:
    '''
    Produz True se algum elemento de *lst* é True,
    Produz False caso contrário
    Exemplos
    >>> algum_true([])
    False
    >>> algum_true([False])
    False
    >>> algum_true([False, True, False])
    True
    '''
    algum_true = False
    for b in lst:
        if b:
            algum_true = True
    return algum_true
