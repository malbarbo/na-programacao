from spython import (
    Image,
    animate,
    square,
    place_image,
    empty_scene,
    fill,
    blue,
)


LARGURA = 200
ALTURA = 60
Q_LADO = 30
LIMITE = LARGURA - Q_LADO


def cena(tick: int) -> Image:
    """Devolve a cena com o quadrado na posição correspondente ao *tick*.
    O quadrado vai da esquerda até a direita e volta, repetindo."""
    # período = 2 * LIMITE: primeira metade indo, segunda voltando
    pos = tick % (2 * LIMITE)
    if pos < LIMITE:
        x = pos
    else:
        x = 2 * LIMITE - pos
    return place_image(
        empty_scene(LARGURA, ALTURA),
        x + Q_LADO // 2,
        ALTURA // 2,
        square(Q_LADO, fill(blue)),
    )


def main() -> None:
    animate(cena)
