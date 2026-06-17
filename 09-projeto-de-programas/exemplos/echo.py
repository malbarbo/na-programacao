# Lê linhas da entrada padrão e as escreve na saída padrão, até o fim da
# entrada (eof).
#
# Para executar:
#
#     python3 echo.py
#     python3 echo.py < teste.txt

import sys


def main() -> None:
    continuar = True
    while continuar:
        linha = sys.stdin.readline()
        if linha != '':
            sys.stdout.write(linha)
        else:
            continuar = False


if __name__ == '__main__':
    main()
