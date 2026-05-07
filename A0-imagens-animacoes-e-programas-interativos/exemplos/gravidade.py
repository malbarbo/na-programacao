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
    x: int
    y: int
    velocidade_x: int
    velocidade_y: int


LARGURA = 200
ALTURA = 200
B_RAIO = 10
B_X_INICIAL = 100
B_Y_INICIAL = 10
B_VX_INICIAL = 15
# pixels por tique^2 (aceleração da gravidade)
ACELERACAO = 2
# pixels por tique (desaceleração horizontal por atrito)
ATRITO = 1
# velocidade vertical abaixo da qual a quicada é tratada como repouso
V_REPOUSO = 4


def desenha(bola: Bola) -> Image:
    return place_image(
        empty_scene(LARGURA, ALTURA),
        bola.x,
        bola.y,
        circle(B_RAIO, fill(blue)),
    )


def avanca(bola: Bola) -> Bola:
    """
    Avança a posição e a velocidade da bola sob ação da gravidade
    (na vertical) e do atrito (na horizontal). Quando a bola passa
    de algum dos limites, inverte a componente correspondente da
    velocidade (perdendo 30% da magnitude no impacto) e a bola
    volta para dentro da cena. Se a quicada vertical não tem
    energia suficiente para vencer a gravidade, a bola fica em
    repouso no chão.

    >>> avanca(Bola(100, 10, 0, 0))
    Bola(x=100, y=11, velocidade_x=0, velocidade_y=2)
    >>> avanca(Bola(100, 11, 0, 2))
    Bola(x=100, y=14, velocidade_x=0, velocidade_y=4)
    >>> avanca(Bola(100, 180, 0, 10))
    Bola(x=100, y=189, velocidade_x=0, velocidade_y=-7)
    >>> avanca(Bola(100, 190, 0, 0))
    Bola(x=100, y=190, velocidade_x=0, velocidade_y=0)
    >>> avanca(Bola(50, 100, 5, 0))
    Bola(x=55, y=101, velocidade_x=4, velocidade_y=2)
    >>> avanca(Bola(195, 100, 5, 0))
    Bola(x=180, y=101, velocidade_x=-2, velocidade_y=2)
    """
    # s = s0 + vt + at^2/2, onde t = 1
    y = bola.y + bola.velocidade_y + ACELERACAO // 2
    # v = v0 + at, onde t = 1
    velocidade_y = bola.velocidade_y + ACELERACAO
    if y > ALTURA - B_RAIO:
        # passou do limite, inverte e reduz a magnitude para 70%
        # (usa a velocidade do início do tique como velocidade de
        # impacto, já que a quicada acontece durante o tique)
        velocidade_y = -(bola.velocidade_y * 7 // 10)
        if velocidade_y >= -V_REPOUSO:
            # quicada sem energia para um salto visível: bola repousa
            velocidade_y = 0
            y = ALTURA - B_RAIO
        else:
            # bola volta para dentro da cena
            y = 2 * (ALTURA - B_RAIO) - y

    x = bola.x + bola.velocidade_x
    # atrito: a velocidade horizontal se aproxima de 0
    if bola.velocidade_x > 0:
        velocidade_x = bola.velocidade_x - ATRITO
    elif bola.velocidade_x < 0:
        velocidade_x = bola.velocidade_x + ATRITO
    else:
        velocidade_x = 0
    if x < B_RAIO:
        # passou do limite esquerdo, inverte e reduz a magnitude para 70%
        velocidade_x = -(velocidade_x * 7 // 10)
        x = 2 * B_RAIO - x
    elif x > LARGURA - B_RAIO:
        # passou do limite direito, inverte e reduz a magnitude para 70%
        velocidade_x = -(velocidade_x * 7 // 10)
        x = 2 * (LARGURA - B_RAIO) - x

    return Bola(x, y, velocidade_x, velocidade_y)


def reseta(bola: Bola, tecla: str) -> Bola:
    """
    Reinicia *bola* na posição e velocidade iniciais se a tecla "r"
    for pressionada, devolve *bola* inalterada para outras teclas.

    >>> reseta(Bola(50, 50, 0, 0), 'r')
    Bola(x=100, y=10, velocidade_x=15, velocidade_y=0)
    >>> reseta(Bola(50, 50, 0, 0), 'ArrowLeft')
    Bola(x=50, y=50, velocidade_x=0, velocidade_y=0)
    """
    if tecla == 'r':
        return Bola(B_X_INICIAL, B_Y_INICIAL, B_VX_INICIAL, 0)
    else:
        return bola


def main() -> None:
    mundo = World(Bola(B_X_INICIAL, B_Y_INICIAL, B_VX_INICIAL, 0), desenha)
    mundo.on_tick(avanca)
    mundo.on_key_down(reseta)
    mundo.run()
