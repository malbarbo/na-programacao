from dataclasses import dataclass
from spython import (
    Image,
    World,
    circle,
    place_image,
    empty_scene,
    fill,
    blue,
)


@dataclass
class Bola:
    y: int
    velocidade: int


LARGURA = 200
ALTURA = 200
B_RAIO = 10
B_X = 100
B_Y_INICIAL = 10
# 2 pixels por tique
ACELERACAO = 2


def desenha(bola: Bola) -> Image:
    return place_image(
        empty_scene(LARGURA, ALTURA),
        B_X,
        bola.y,
        circle(B_RAIO, fill(blue)),
    )


def avanca(bola: Bola) -> Bola:
    """
    Avança a posição e velocidade da bola sob ação da gravidade.
    Quando a bola passa do limite inferior, inverte a velocidade
    (perdendo 30% no impacto) e a bola volta para dentro da cena.

    >>> avanca(Bola(10, 0))
    Bola(y=11, velocidade=2)
    >>> avanca(Bola(11, 2))
    Bola(y=14, velocidade=4)
    >>> avanca(Bola(190, 0))
    Bola(y=189, velocidade=-2)
    """
    # s = s0 + vt + at^2/2, onde t = 1
    y = bola.y + bola.velocidade + ACELERACAO // 2
    # v = v0 + at, onde t = 1
    velocidade = bola.velocidade + ACELERACAO
    if y > ALTURA - B_RAIO:
        # passou do limite, a velocidade muda de direção e o módulo diminui
        velocidade = velocidade * -7 // 10
        # a bola volta para dentro da cena
        y = 2 * (ALTURA - B_RAIO) - y
    return Bola(y, velocidade)


def reseta(bola: Bola, tecla: str) -> Bola:
    """
    Reinicia *bola* na posição inicial se a tecla "r" for pressionada,
    devolve *bola* inalterada para outras teclas.

    >>> reseta(Bola(50, 5), 'r')
    Bola(y=10, velocidade=0)
    >>> reseta(Bola(50, 5), 'ArrowLeft')
    Bola(y=50, velocidade=5)
    """
    if tecla == 'r':
        return Bola(B_Y_INICIAL, 0)
    else:
        return bola


def main() -> None:
    mundo = World(Bola(B_Y_INICIAL, 0), desenha)
    mundo.on_tick(avanca)
    mundo.on_key_down(reseta)
    mundo.run()
