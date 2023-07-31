def main():
    # Entrada
    numero: int = int(input('Digite um número inteiro: '))

    # Processamento
    d: int = dobro(numero)

    # Saída
    print('O dobro de', numero, 'é', d)


def dobro(x: int) -> int:
    '''
    Calcula o dobro de x.

    Exemplo
    >>> dobro(4)
    8
    '''
    return 2 * x


if __name__ == '__main__':
    main()
