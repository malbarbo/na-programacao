# Análise
#
# Calcular o rendimento em um investimento durante um ano.
# A taxa depende do valor investido.
# valor <= 2000, 10%
# 2000 < valor <= 5000, 12%
# valor > 5000, 13%

# Definição de tipos de dados
#
# O valor investido e o rendimento são números positivos.

def rendimento(valor: float) -> float:
    '''
    Determina quanto o investimento de *valor* renderá
    em um ano considerando as seguintes taxas:
    - valor <= 2000, 10%
    - 2000 < valor <= 5000, 12%
    - valor > 5000, 13%

    Exemplos
    >>> rendimento(1000.0)
    100.0
    >>> rendimento(2000.0)
    200.0
    >>> rendimento(4000.0)
    480.0
    >>> rendimento(5000.0)
    600.0
    >>> rendimento(6000.0)
    780.0
    '''
    if valor <= 2000.0:
        r = valor * 0.1
    elif valor <= 5000.0:
        r = valor * 0.12
    else:
        r = valor * 0.13
    return r
