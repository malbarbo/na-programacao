from dataclasses import dataclass
from enum import Enum, auto
from spython import (
    Color,
    Image,
    World,
    square,
    put_image,
    empty_scene,
    fill,
    green,
    red,
    yellow,
)


class Cor(Enum):
    VERDE = auto()
    VERMELHO = auto()
    AMARELO = auto()


@dataclass
class Quadrado:
    x: int
    cor: Cor


LARGURA = 100
ALTURA = 100
DESLOCAMENTO = 10
Q_LADO = 20
Q_Y = 50
Q_X_INICIAL = 50


def cor_para_fill(cor: Cor) -> Color:
    if cor == Cor.VERDE:
        return green
    elif cor == Cor.VERMELHO:
        return red
    else:
        return yellow


def desenha(q: Quadrado) -> Image:
    return put_image(
        empty_scene(LARGURA, ALTURA),
        q.x,
        Q_Y,
        square(Q_LADO, fill(cor_para_fill(q.cor))),
    )


def move(q: Quadrado, tecla: str) -> Quadrado:
    """
    Desloca *q* para a esquerda (subtrai *DESLOCAMENTO* de *x*) se *tecla* for
    "ArrowLeft" e para a direita (soma *DESLOCAMENTO* a *x*) se *tecla* for
    "ArrowRight". Devolve *q* para outras teclas.

    >>> move(Quadrado(50, Cor.VERDE), 'ArrowLeft')
    Quadrado(x=40, cor=<Cor.VERDE: 1>)
    >>> move(Quadrado(50, Cor.VERDE), 'ArrowRight')
    Quadrado(x=60, cor=<Cor.VERDE: 1>)
    >>> move(Quadrado(50, Cor.VERDE), 'Space')
    Quadrado(x=50, cor=<Cor.VERDE: 1>)
    """
    if tecla == 'ArrowLeft':
        return Quadrado(q.x - DESLOCAMENTO, q.cor)
    elif tecla == 'ArrowRight':
        return Quadrado(q.x + DESLOCAMENTO, q.cor)
    else:
        return q


def muda_cor(q: Quadrado) -> Quadrado:
    """
    Muda a cor de *q* da seguinte forma:
    Verde -> Amarelo
    Amarelo -> Vermelho
    Vermelho -> Verde

    >>> muda_cor(Quadrado(50, Cor.VERDE))
    Quadrado(x=50, cor=<Cor.AMARELO: 3>)
    >>> muda_cor(Quadrado(50, Cor.AMARELO))
    Quadrado(x=50, cor=<Cor.VERMELHO: 2>)
    >>> muda_cor(Quadrado(50, Cor.VERMELHO))
    Quadrado(x=50, cor=<Cor.VERDE: 1>)
    """
    if q.cor == Cor.VERDE:
        nova = Cor.AMARELO
    elif q.cor == Cor.AMARELO:
        nova = Cor.VERMELHO
    else:
        nova = Cor.VERDE
    return Quadrado(q.x, nova)


def main() -> None:
    mundo = World(Quadrado(Q_X_INICIAL, Cor.VERDE), desenha)
    mundo.on_key_down(move)
    mundo.on_tick(muda_cor)
    mundo.tick_rate(1)
    mundo.run()
