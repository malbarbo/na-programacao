from spython import star, fill, firebrick, to_svg


def main() -> None:
    print(to_svg(star(40, fill(firebrick))))
