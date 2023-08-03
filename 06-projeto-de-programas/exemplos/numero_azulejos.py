import math

# Análise
#
# Calcular o número de azulejos necessários para azulejar uma parede com
# determinado comprimento e altura, considerando que cada azulejo mede
# 0,2m x 0,2m e que nenhum azulejo é perdido e que recortes são descartados.

# Tipos de dados
#
# A largura e a altura são dados em metros e representadas com números
# positivos.

def numero_azulejos(comprimento: float, altura: float) -> int:
    '''
    Calcula o número de azulejos de 0,2mx0,2m necessários para azulejar uma
    pare de tamanho *comprimento* x *altura* (em metros) considerando que
    nenhum azulejo é perdido e que recortes são descartados.

    Exemplos
    >>> numero_azulejos(2.0, 2.4)
    120
    >>> numero_azulejos(1.5, 2.3)
    96

    Algumas situações particulares
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
