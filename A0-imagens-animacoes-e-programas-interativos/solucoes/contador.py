from spython import (
    Image,
    World,
    text,
    overlay,
    empty_scene,
    fill,
    black,
)


LARGURA = 200
ALTURA = 100


def desenha(n: int) -> Image:
    return overlay(text(str(n), fill(black), size=40), empty_scene(LARGURA, ALTURA))


def trata_tecla(n: int, tecla: str) -> int:
    """
    Incrementa *n* se *tecla* for "+", decrementa se for "-",
    devolve *n* inalterado para outras teclas.

    >>> trata_tecla(5, '+')
    6
    >>> trata_tecla(5, '-')
    4
    >>> trata_tecla(5, 'Enter')
    5
    """
    if tecla == '+':
        return n + 1
    elif tecla == '-':
        return n - 1
    else:
        return n


def main() -> None:
    mundo = World(0, desenha)
    mundo.on_key_down(trata_tecla)
    mundo.run()
