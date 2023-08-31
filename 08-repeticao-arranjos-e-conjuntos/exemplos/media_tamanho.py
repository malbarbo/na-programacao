def media_tamanho(lst: list[str]) -> float:
    '''
    Calcula a média dos tamanhos das strings de *lst*.
    Requer que *lst* seja não vazia.

    Exemplos
    >>> media_tamanho(['casa'])
    4.0
    >>> media_tamanho(['casa', 'da'])
    3.0
    >>> media_tamanho(['casa', 'da', ''])
    2.0
    >>> media_tamanho(['casa', 'da', '', 'onça'])
    2.5
    '''
    assert len(lst) != 0

    # Soma dos tamanhos
    soma = 0
    for s in lst:
        soma = soma + len(s)

    # Média
    return soma / len(lst)
