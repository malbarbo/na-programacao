def ponto_final(texto: str) -> str:
    """
    Produz *texto* se *texto* é vazio ou termina com ponto final, caso
    contrário, produz *texto* concatenado com '.'.

    Exemplos
    >>> # Não adiciona o ponto
    >>> ponto_final('')
    ''
    >>> ponto_final('Talvez.')
    'Talvez.'
    >>> # Adiciona ponto
    >>> ponto_final('Sim, eu gostaria')
    'Sim, eu gostaria.'
    """
    if texto == '':
        com_ponto = ''
    elif texto[len(texto) - 1] == '.':
        com_ponto = texto
    else:
        com_ponto = texto + '.'
    return com_ponto
