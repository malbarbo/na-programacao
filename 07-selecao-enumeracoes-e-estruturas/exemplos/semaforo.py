from enum import Enum, auto


class Cor(Enum):
    '''O cor de um semáforo de trânsito.'''
    VERDE = auto()
    VERMELHO = auto()
    AMARELO = auto()


def proxima_cor(atual: Cor) -> Cor:
    '''
    Produz a pŕoxima cor de uma semáfaro que está na cor *atual*.

    Exemplos
    >>> proxima_cor(Cor.VERDE).name
    'AMARELO'
    >>> proxima_cor(Cor.AMARELO).name
    'VERMELHO'
    >>> proxima_cor(Cor.VERMELHO).name
    'VERDE'
    '''
    if atual == Cor.VERDE:
        proxima = Cor.AMARELO
    elif atual == Cor.AMARELO:
        proxima = Cor.VERMELHO
    elif atual == Cor.VERMELHO:
        proxima = Cor.VERDE
    return proxima
