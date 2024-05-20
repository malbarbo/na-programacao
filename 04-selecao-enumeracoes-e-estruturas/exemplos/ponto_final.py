# Análise
#
# Colocar um ponto final em um texto caso ele não termine com um.

# Definição de tipos de dados
#
# O texto é representado por uma string

def ponto_final(texto: str) -> str:
    '''
    Produz *texto* se *texto* é vazio ou termina com ponto final, caso
    contrário, produz *texto* concatenado com '.'.

    Exemplos

    Adiciona o ponto

    >>> ponto_final('Sim, eu gostaria')
    'Sim, eu gostaria.'

    Não adiciona o ponto
    >>> ponto_final('')
    ''
    >>> ponto_final('Talvez.')
    'Talvez.'
    '''
    if texto == '' or texto[-1] == '.':
        com_ponto = texto
    else:
        com_ponto = texto + '.'
    return com_ponto
