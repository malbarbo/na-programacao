def main():
    print('Este programa zera a dezena e unidade de um número natural.')

    # Entrada
    n: int = int(input('Digite um número natural: '))

    # Processamento
    zerado = zera_dezena_e_unidade(n)

    # Saída
    print(n, 'com unidade e dezena zerados é', zerado)


def zera_dezena_e_unidade(n: int) -> int:
    '''
    Zera a dezena e unidade de n.

    >>> zera_dezena_e_unidade(19)
    0
    >>> zera_dezena_e_unidade(341)
    300
    >>> zera_dezena_e_unidade(5251)
    5200
    '''
    return n // 100 * 100


if __name__ == '__main__':
    main()
