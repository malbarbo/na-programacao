# Análise
#
# Rotacionar uma string a direita n caracteres, isto é, mover
# os últimos n caracteres para o início da string.

def rotaciona_direita(s: str, n: int) -> str:
    '''
    Produz uma string movendo os últimos *n* caracteres de *s* para o início de
    *s*. Se *n* é maior do que a quantidade de caracteres de *s* ou é um valor
    negativo, então rotaciona (n % len(s)) caracteres.

    Exemplos:
    >>> rotaciona_direita('marcelio', 5)
    'celiomar'
    >>> rotaciona_direita('abc', 0)
    'abc'
    >>> rotaciona_direita('abc', 1)
    'cab'
    >>> rotaciona_direita('abc', 2)
    'bca'
    >>> rotaciona_direita('abc', 3)
    'abc'
    >>> rotaciona_direita('abc', -1)
    'bca'
    >>> rotaciona_direita('abc', -2)
    'cab'
    >>> rotaciona_direita('abc', -3)
    'abc'
    '''
    div = len(s) - n % len(s)
    return s[div:] + s[:div]
