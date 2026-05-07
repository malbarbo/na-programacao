"""Gera o PDF da tabela de cores nomeadas do spython.

Saída: bytes do PDF em stdout (consumido pelo filtro lua de imagens).
Layout: 7 colunas × 21 linhas. Para manter contraste, o nome da cor é
desenhado em branco sobre cores escuras e em preto sobre cores claras,
de acordo com a luminância relativa.
"""

import sys
from spython import (
    Color,
    Image,
    text,
    rectangle,
    overlay,
    above,
    beside,
    fill,
    to_pdf,
    aliceblue, antiquewhite, aqua, aquamarine, azure,
    beige, bisque, black, blanchedalmond, blue, blueviolet, brown, burlywood,
    cadetblue, chartreuse, chocolate, coral, cornflowerblue, cornsilk,
    crimson, cyan,
    darkblue, darkcyan, darkgoldenrod, darkgray, darkgreen, darkgrey,
    darkkhaki, darkmagenta, darkolivegreen, darkorange, darkorchid, darkred,
    darksalmon, darkseagreen, darkslateblue, darkslategray, darkslategrey,
    darkturquoise, darkviolet, deeppink, deepskyblue, dimgray, dimgrey,
    dodgerblue,
    firebrick, floralwhite, forestgreen, fuchsia,
    gainsboro, ghostwhite, gold, goldenrod, gray, green, greenyellow, grey,
    honeydew, hotpink,
    indianred, indigo, ivory,
    khaki,
    lavender, lavenderblush, lawngreen, lemonchiffon, lightblue, lightcoral,
    lightcyan, lightgoldenrodyellow, lightgray, lightgreen, lightgrey,
    lightpink, lightsalmon, lightseagreen, lightskyblue, lightslategray,
    lightslategrey, lightsteelblue, lightyellow, lime, limegreen, linen,
    magenta, maroon, mediumaquamarine, mediumblue, mediumorchid, mediumpurple,
    mediumseagreen, mediumslateblue, mediumspringgreen, mediumturquoise,
    mediumvioletred, midnightblue, mintcream, mistyrose, moccasin,
    navajowhite, navy,
    oldlace, olive, olivedrab, orange, orangered, orchid,
    palegoldenrod, palegreen, paleturquoise, palevioletred, papayawhip,
    peachpuff, peru, pink, plum, powderblue, purple,
    red, rosybrown, royalblue,
    saddlebrown, salmon, sandybrown, seagreen, seashell, sienna, silver,
    skyblue, slateblue, slategray, slategrey, snow, springgreen, steelblue,
    tan, teal, thistle, tomato, turquoise,
    violet,
    wheat, white, whitesmoke,
    yellow, yellowgreen,
)


LARGURA_CELULA = 220
ALTURA_CELULA = 30
TAMANHO_FONTE = 14


# Ordem coluna por coluna, mesma que aparece nos slides.
COLUNAS: list[list[tuple[str, Color]]] = [
    [
        ('white', white),
        ('snow', snow),
        ('ghostwhite', ghostwhite),
        ('whitesmoke', whitesmoke),
        ('floralwhite', floralwhite),
        ('oldlace', oldlace),
        ('ivory', ivory),
        ('honeydew', honeydew),
        ('mintcream', mintcream),
        ('azure', azure),
        ('beige', beige),
        ('aliceblue', aliceblue),
        ('antiquewhite', antiquewhite),
        ('linen', linen),
        ('lavender', lavender),
        ('lavenderblush', lavenderblush),
        ('mistyrose', mistyrose),
        ('gainsboro', gainsboro),
        ('lightgray', lightgray),
        ('lightgrey', lightgrey),
        ('silver', silver),
    ],
    [
        ('darkgray', darkgray),
        ('darkgrey', darkgrey),
        ('gray', gray),
        ('grey', grey),
        ('dimgray', dimgray),
        ('dimgrey', dimgrey),
        ('slategray', slategray),
        ('slategrey', slategrey),
        ('lightslategray', lightslategray),
        ('lightslategrey', lightslategrey),
        ('darkslategray', darkslategray),
        ('darkslategrey', darkslategrey),
        ('black', black),
        ('red', red),
        ('crimson', crimson),
        ('deeppink', deeppink),
        ('hotpink', hotpink),
        ('pink', pink),
        ('lightpink', lightpink),
        ('palevioletred', palevioletred),
        ('maroon', maroon),
    ],
    [
        ('darkred', darkred),
        ('firebrick', firebrick),
        ('indianred', indianred),
        ('brown', brown),
        ('sienna', sienna),
        ('rosybrown', rosybrown),
        ('salmon', salmon),
        ('lightsalmon', lightsalmon),
        ('darksalmon', darksalmon),
        ('coral', coral),
        ('lightcoral', lightcoral),
        ('tomato', tomato),
        ('orangered', orangered),
        ('saddlebrown', saddlebrown),
        ('chocolate', chocolate),
        ('sandybrown', sandybrown),
        ('peru', peru),
        ('orange', orange),
        ('darkorange', darkorange),
        ('goldenrod', goldenrod),
        ('darkgoldenrod', darkgoldenrod),
    ],
    [
        ('gold', gold),
        ('yellow', yellow),
        ('lightyellow', lightyellow),
        ('lemonchiffon', lemonchiffon),
        ('lightgoldenrodyellow', lightgoldenrodyellow),
        ('papayawhip', papayawhip),
        ('seashell', seashell),
        ('moccasin', moccasin),
        ('peachpuff', peachpuff),
        ('bisque', bisque),
        ('blanchedalmond', blanchedalmond),
        ('cornsilk', cornsilk),
        ('navajowhite', navajowhite),
        ('wheat', wheat),
        ('burlywood', burlywood),
        ('tan', tan),
        ('darkkhaki', darkkhaki),
        ('khaki', khaki),
        ('palegoldenrod', palegoldenrod),
        ('greenyellow', greenyellow),
        ('chartreuse', chartreuse),
    ],
    [
        ('lawngreen', lawngreen),
        ('lime', lime),
        ('limegreen', limegreen),
        ('seagreen', seagreen),
        ('forestgreen', forestgreen),
        ('darkgreen', darkgreen),
        ('green', green),
        ('mediumseagreen', mediumseagreen),
        ('mediumspringgreen', mediumspringgreen),
        ('springgreen', springgreen),
        ('palegreen', palegreen),
        ('lightgreen', lightgreen),
        ('darkolivegreen', darkolivegreen),
        ('olivedrab', olivedrab),
        ('yellowgreen', yellowgreen),
        ('olive', olive),
        ('darkseagreen', darkseagreen),
        ('lightseagreen', lightseagreen),
        ('cadetblue', cadetblue),
        ('teal', teal),
        ('aqua', aqua),
    ],
    [
        ('cyan', cyan),
        ('lightcyan', lightcyan),
        ('paleturquoise', paleturquoise),
        ('aquamarine', aquamarine),
        ('turquoise', turquoise),
        ('mediumturquoise', mediumturquoise),
        ('darkturquoise', darkturquoise),
        ('darkcyan', darkcyan),
        ('mediumaquamarine', mediumaquamarine),
        ('steelblue', steelblue),
        ('lightsteelblue', lightsteelblue),
        ('powderblue', powderblue),
        ('lightblue', lightblue),
        ('skyblue', skyblue),
        ('lightskyblue', lightskyblue),
        ('deepskyblue', deepskyblue),
        ('dodgerblue', dodgerblue),
        ('cornflowerblue', cornflowerblue),
        ('royalblue', royalblue),
        ('blue', blue),
        ('mediumblue', mediumblue),
    ],
    [
        ('darkblue', darkblue),
        ('navy', navy),
        ('midnightblue', midnightblue),
        ('purple', purple),
        ('indigo', indigo),
        ('blueviolet', blueviolet),
        ('darkviolet', darkviolet),
        ('darkslateblue', darkslateblue),
        ('mediumslateblue', mediumslateblue),
        ('plum', plum),
        ('slateblue', slateblue),
        ('mediumpurple', mediumpurple),
        ('thistle', thistle),
        ('violet', violet),
        ('orchid', orchid),
        ('mediumorchid', mediumorchid),
        ('darkorchid', darkorchid),
        ('magenta', magenta),
        ('fuchsia', fuchsia),
        ('darkmagenta', darkmagenta),
        ('mediumvioletred', mediumvioletred),
    ],
]


def luminancia(cor: Color) -> float:
    return (0.2126 * cor.r + 0.7152 * cor.g + 0.0722 * cor.b) / 255


def celula(nome: str, cor: Color) -> Image:
    if luminancia(cor) < 0.5:
        cor_texto = white
    else:
        cor_texto = black
    return overlay(
        text(nome, fill(cor_texto), size=TAMANHO_FONTE),
        rectangle(LARGURA_CELULA, ALTURA_CELULA, fill(cor)),
    )


def coluna(cores: list[tuple[str, Color]]) -> Image:
    img = celula(cores[0][0], cores[0][1])
    for nome, cor in cores[1:]:
        img = above(img, celula(nome, cor))
    return img


def grade() -> Image:
    img = coluna(COLUNAS[0])
    for col in COLUNAS[1:]:
        img = beside(img, coluna(col))
    return img


sys.stdout.buffer.write(to_pdf(grade()))
