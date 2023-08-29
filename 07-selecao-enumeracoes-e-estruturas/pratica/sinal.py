# Análise
#
# Determinar o sinal de um número inteiro.
#   -1 para negativos
#   0 para 0
#   +1 para positivos

def sinal(n: int) -> int:
    '''
    Determina o sinal de *n*.
    Se n < 0, produz -1.
    Se n == 0, produz 0.
    Se ne > 0, produz 1.

    Exemplos
    >>> sinal(-6)
    -1
    >>> sinal(0)
    0
    >>> sinal(10)
    1
    '''
    if n < 0:
        s = -1
    elif n == 0:
        s = 0
    else:
        s = 1
    return s
