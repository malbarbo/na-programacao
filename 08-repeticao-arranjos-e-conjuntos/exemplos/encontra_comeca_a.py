def encontra_comeca_a(lst: list[str]) -> list[str]:
    '''
    Encontra os elementos de *lst* que começam com 'A'.

    Exemplos
    >>> encontra_comeca_a([])
    []
    >>> encontra_comeca_a(['Ali'])
    ['Ali']
    >>> encontra_comeca_a(['Ali', 'ala'])
    ['Ali']
    >>> encontra_comeca_a(['Ali', 'ala', 'Alto'])
    ['Ali', 'Alto']
    >>> encontra_comeca_a(['Ali', 'ala', 'Alto', ''])
    ['Ali', 'Alto']
    '''
    comeca_a = []
    for s in lst:
        if s != '' and s[0] == 'A':
            comeca_a.append(s)
    return comeca_a
