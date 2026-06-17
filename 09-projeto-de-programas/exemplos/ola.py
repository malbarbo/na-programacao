# Exibe uma saudação para cada nome informado na linha de comando.
# Sem argumentos, saúda o mundo.
#
# Para executar:
#
#     python3 ola.py
#     python3 ola.py José "Ana Maria"

import sys


def main() -> None:
    if len(sys.argv) <= 1:
        print(ola('mundo'))
    else:
        for nome in sys.argv[1:]:
            print(ola(nome))


def ola(nome: str) -> str:
    '''
    Devolve uma saudação para *nome*.
    >>> ola('mundo')
    'Olá mundo!'
    >>> ola('José')
    'Olá José!'
    '''
    return 'Olá ' + nome + '!'


if __name__ == '__main__':
    main()
