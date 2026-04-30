from spython import (
    Image,
    animate,
    circle,
    rectangle,
    overlay,
    empty_scene,
    place_image,
    fill,
    green,
)


def cena_ovni(tick: int) -> Image:
    ovni = overlay(circle(10, fill(green)), rectangle(40, 4, fill(green)))
    return place_image(empty_scene(100, 100), 50, tick, ovni)


def main() -> None:
    animate(cena_ovni)
