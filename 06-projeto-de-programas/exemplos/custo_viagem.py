# Análise
#
# Calcular o custo em reais para percorrer uma determinada distância levando em
# consideração o desempenho do carro e o preço do litro do combustível.

# Tipos de Dados
#
# Distância, redimento, preço do litro e custo são representado por números
# positivos.

def custo_viagem(distancia: float, rendimento: float, preco: float) -> float:
    '''
    Calcula o custo em reais para percorrer a *distancia* especificada
    considerando o *rendimento* do carro e o *preco* do litro do combustível.

    Exemplos
    >>> # (120.0 / 10.0) * 5.0
    >>> custo_viagem(120.0, 10.0, 5.0)
    60.0
    >>> # (300.0 / 15.0) * 6.0
    >>> custo_viagem(300.0, 15.0, 6.0)
    120.0
    '''
    return (distancia / rendimento) * preco
