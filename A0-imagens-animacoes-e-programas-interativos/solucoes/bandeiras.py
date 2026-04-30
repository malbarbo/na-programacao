from spython import (
    Image,
    above,
    beside,
    overlay,
    rectangle,
    circle,
    square,
    rhombus,
    star,
    fill,
    white,
    red,
    green,
    blue,
    yellow,
    black,
    gold,
)


def japao() -> Image:
    """Bandeira do Japão: círculo vermelho centralizado em um fundo branco."""
    return overlay(circle(60, fill(red)), rectangle(300, 200, fill(white)))


def italia() -> Image:
    """Bandeira da Itália: três faixas verticais — verde, branco, vermelho."""
    return beside(
        beside(rectangle(80, 200, fill(green)), rectangle(80, 200, fill(white))),
        rectangle(80, 200, fill(red)),
    )


def alemanha() -> Image:
    """Bandeira da Alemanha: três faixas horizontais — preto, vermelho, dourado."""
    return above(
        above(rectangle(300, 60, fill(black)), rectangle(300, 60, fill(red))),
        rectangle(300, 60, fill(gold)),
    )


def chile() -> Image:
    """Bandeira do Chile: quadrado azul com estrela branca, faixa branca e
    faixa vermelha."""
    quadrado = overlay(star(20, fill(white)), square(100, fill(blue)))
    metade_superior = beside(quadrado, rectangle(200, 100, fill(white)))
    return above(metade_superior, rectangle(300, 100, fill(red)))


def dinamarca() -> Image:
    """Bandeira da Dinamarca (simplificada): cruz branca centralizada
    em fundo vermelho."""
    cruz = overlay(rectangle(30, 200, fill(white)), rectangle(300, 30, fill(white)))
    return overlay(cruz, rectangle(300, 200, fill(red)))


def brasil() -> Image:
    """Bandeira do Brasil simplificada: losango amarelo sobre retângulo verde,
    círculo azul no centro."""
    return overlay(
        circle(35, fill(blue)),
        overlay(
            rhombus(220, 90, fill(yellow)),
            rectangle(300, 210, fill(green)),
        ),
    )
