from spython import (
    Font,
    Image,
    animate,
    text,
    beside,
    overlay,
    empty_scene,
    fill,
    black,
    red,
)


def cena_texto(tick: int) -> Image:
    FONTE = Font(family='monospace', size=30)
    PALAVRA = 'computação'
    # dividimos por 10 para desacelerar a animação
    i = tick // 10 % len(palavra)
    inicio = PALAVRA[:i]
    letra = PALAVRA[i:i + 1]
    fim = PALAVRA[i + 1:]
    t = beside(text(inicio, fill(black), font=FONTE), text(letra, fill(red), font=FONTE))
    t = beside(t, text(fim, fill(black), font=FONTE))
    return overlay(t, empty_scene(230, 50))


def main() -> None:
    animate(cena_texto)
