def conta_zeros(m: list[list[int]]) -> int:
    '''
    Conta a quantidade de zeros da matriz *m*.

    Exemplos
    >>> conta_zeros([[1, 0, 7], [0, 1, 0]])
    3
    >>> conta_zeros([[1, 0], [1, 2], [0, 2]])
    2
    '''
    num_zeros = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 0:
                num_zeros = num_zeros + 1
    return num_zeros


def conta_zeros2(m: list[list[int]]) -> int:
    '''
    Conta a quantidade de zeros da matriz *m*.

    Exemplos
    >>> conta_zeros2([[1, 0, 7], [0, 1, 0]])
    3
    >>> conta_zeros2([[1, 0], [1, 2], [0, 2]])
    2
    '''
    num_zeros = 0
    for linha in m:
        for elem in linha:
            if elem == 0:
                num_zeros = num_zeros + 1
    return num_zeros
