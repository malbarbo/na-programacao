from spython import (
    Image,
    animate,
    circle,
    place_image,
    empty_scene,
    fill,
    red,
)


LARGURA = 150
ALTURA = 150
RAIO_MIN = 10
RAIO_MAX = 60
INTERVALO = RAIO_MAX - RAIO_MIN


def cena(tick: int) -> Image:
    """
    Devolve a cena com o círculo no raio correspondente ao *tick*.
    O raio cresce de RAIO_MIN até RAIO_MAX e depois decresce, repetindo.
    """
    pos = tick % (2 * INTERVALO)
    if pos < INTERVALO:
        raio = RAIO_MIN + pos
    else:
        raio = RAIO_MIN + 2 * INTERVALO - pos
    return place_image(
        empty_scene(LARGURA, ALTURA), LARGURA // 2, ALTURA // 2, circle(raio, fill(red))
    )


def main() -> None:
    animate(cena)
