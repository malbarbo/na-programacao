def eh_regular(a: list[list[int]]) -> bool:
    '''
    Produz True se *a* é uma matriz regular, isso é, todas as linhas tem a
    mesma quantidade de elementos.

    Requer que len(a) > 0.

    Exemplo
    >>> eh_regular([[2]])
    True
    >>> eh_regular([[2], [4]])
    True
    >>> eh_regular([[2], [4, 1]])
    False
    >>> eh_regular([[2, 2], [4]])
    False
    >>> eh_regular([[2, 1, 6], [4, 0, 1]])
    True
    >>> eh_regular([[2, 1], [4, 0, 1]])
    False
    >>> eh_regular([[2, 1], [4]])
    False
    >>> eh_regular([[2], [4], [7]])
    True
    >>> eh_regular([[2], [4], [7, 2]])
    False
    '''
    assert len(a) > 0
    regular = True
    i = 1
    while i < len(a) and regular:
        if len(a[0]) != len(a[i]):
            regular = False
        i = i + 1
    return regular



