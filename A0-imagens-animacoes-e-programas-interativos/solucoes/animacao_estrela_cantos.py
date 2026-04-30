from spython import (
    Image,
    animate,
    star,
    place_image,
    empty_scene,
    fill,
    gold,
)


LARGURA = 200
ALTURA = 200
MARGEM = 30
TICKS_POR_LADO = 50


def cena(tick: int) -> Image:
    """
    Devolve a cena com a estrela percorrendo os quatro cantos do quadrado.
    Cada lado é percorrido em TICKS_POR_LADO tiques.
    """
    lado = (tick // TICKS_POR_LADO) % 4
    progresso = tick % TICKS_POR_LADO
    distancia = LARGURA - 2 * MARGEM
    delta = progresso * distancia // TICKS_POR_LADO
    if lado == 0:
        # superior: esquerda -> direita
        x = MARGEM + delta
        y = MARGEM
    elif lado == 1:
        # direita: cima -> baixo
        x = LARGURA - MARGEM
        y = MARGEM + delta
    elif lado == 2:
        # inferior: direita -> esquerda
        x = LARGURA - MARGEM - delta
        y = ALTURA - MARGEM
    else:
        # esquerda: baixo -> cima
        x = MARGEM
        y = ALTURA - MARGEM - delta
    return place_image(empty_scene(LARGURA, ALTURA), x, y, star(15, fill(gold)))


def main() -> None:
    animate(cena)
