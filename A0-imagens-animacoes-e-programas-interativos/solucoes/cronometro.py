from dataclasses import dataclass
from spython import (
    Image,
    World,
    text,
    overlay,
    empty_scene,
    fill,
    black,
)


LARGURA = 240
ALTURA = 100
TICKS_POR_SEGUNDO = 28


@dataclass
class Cronometro:
    """Estado do cronômetro: *segundos* exibidos e se está *pausado*.
    O contador interno *frames* acumula tiques até completar 1 segundo."""

    segundos: int
    frames: int
    pausado: bool


def desenha(c: Cronometro) -> Image:
    return overlay(
        text(f'{c.segundos:03d}', fill(black), size=50), empty_scene(LARGURA, ALTURA)
    )


def avanca(c: Cronometro) -> Cronometro:
    """
    Avança o cronômetro em um tique. Se pausado, devolve *c* inalterado.
    Caso contrário, incrementa frames e, ao completar TICKS_POR_SEGUNDO,
    incrementa segundos.

    >>> avanca(Cronometro(0, 0, True))
    Cronometro(segundos=0, frames=0, pausado=True)
    >>> avanca(Cronometro(0, 27, False))
    Cronometro(segundos=1, frames=0, pausado=False)
    >>> avanca(Cronometro(0, 5, False))
    Cronometro(segundos=0, frames=6, pausado=False)
    """
    if c.pausado:
        return c
    novos_frames = c.frames + 1
    if novos_frames >= TICKS_POR_SEGUNDO:
        return Cronometro(c.segundos + 1, 0, c.pausado)
    else:
        return Cronometro(c.segundos, novos_frames, c.pausado)


def trata_tecla(c: Cronometro, tecla: str) -> Cronometro:
    """
    "p" alterna pausa/continua, "z" zera o cronômetro mantendo o estado de
    pausa, "r" reinicia (zera e despausado). Outras teclas devolvem *c*.

    >>> trata_tecla(Cronometro(5, 0, False), 'p')
    Cronometro(segundos=5, frames=0, pausado=True)
    >>> trata_tecla(Cronometro(5, 10, True), 'z')
    Cronometro(segundos=0, frames=0, pausado=True)
    >>> trata_tecla(Cronometro(5, 10, True), 'r')
    Cronometro(segundos=0, frames=0, pausado=False)
    >>> trata_tecla(Cronometro(5, 10, False), 'Enter')
    Cronometro(segundos=5, frames=10, pausado=False)
    """
    if tecla == 'p':
        return Cronometro(c.segundos, c.frames, not c.pausado)
    elif tecla == 'z':
        return Cronometro(0, 0, c.pausado)
    elif tecla == 'r':
        return Cronometro(0, 0, False)
    else:
        return c


def main() -> None:
    mundo = World(Cronometro(0, 0, False), desenha)
    mundo.on_tick(avanca)
    mundo.on_key_down(trata_tecla)
    mundo.run()
