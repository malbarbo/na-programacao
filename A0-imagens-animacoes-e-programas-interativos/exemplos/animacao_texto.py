from spython import (
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
    palavra = 'computação'
    # dividimos por 10 para desacelerar a animação
    i = tick // 10 % len(palavra)
    inicio = palavra[:i]
    letra = palavra[i : i + 1]
    fim = palavra[i + 1 :]
    t = beside(text(inicio, fill(black), size=30), text(letra, fill(red), size=30))
    t = beside(t, text(fim, fill(black), size=30))
    return overlay(t, empty_scene(230, 50))


def main() -> None:
    animate(cena_texto)
