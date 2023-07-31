import math

def numero_azulejos(comprimento: float, altura: float) -> int:
    '''
    Calcula o número de azulejos de 0,2mx0,2m necessários para azulejar uma
    area de tamanho *comprimento* x *altura* (em metros) considerando que
    nenhum azulejo é perdido e que recortes são descartados.

    Exemplos
    >>> numero_azulejos(2.0, 2.4)
    120
    >>> numero_azulejos(1.5, 2.3)
    96
    >>> # Alguns casos extremos
    >>> numero_azulejos(0.2, 0.2)
    1
    >>> numero_azulejos(0.3, 0.2)
    2
    >>> numero_azulejos(0.3, 0.3)
    4
    >>> numero_azulejos(0.4, 0.4)
    4
    '''
    return math.ceil(comprimento / 0.2) * math.ceil(altura / 0.2)
