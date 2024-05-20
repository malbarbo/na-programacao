# Análise
#
# Calcular a massa de um tubo de ferro a partir das suas dimensões.
# O volume de um tudo de ferro é dado por
# pi * [(diametro_externo - diametro_interno) / 2] ** 2 * altura
# A massa de um objeto pode ser calculada com massa * densidade
# A densidade do ferro é 7874 kg/m3

# Tipos de dados
#
# As dimensões do tubo são dadas em metros e representadas por números positivos
# A massa é dada em kilograma e representado por um número positivo

PI: float = 3.14
DENSIDADE_FERRO: float = 7874

def massa_tubo_ferro(diametro_externo: float, diametro_interno: float, altura: float) -> float:
    '''
    Calcula a massa de um tubo de ferro a partir das suas dimensões.

    Requer diametro_externo > diametro-interno.

    Exemplos
    >>> # 3.14 * ((0.05 - 0.03) / 2) ** 2 * 0.1 * 7874
    >>> round(massa_tubo_ferro(0.05, 0.03, 0.1), 7)
    0.2472436
    '''
    area = PI * ((diametro_externo - diametro_interno) / 2) ** 2
    volume = area * altura
    return volume * DENSIDADE_FERRO
