def main():
    print('Este programa muda uma frase deixando apenas a primeira letra em maiúscula.')

    # Entrada
    frase: str = input('Digite uma frase: ')

    # Processamento
    frasem = primeira_maiuscula(frase)

    # Saída
    print('Frase modificada:', frasem)


def primeira_maiuscula(frase: str) -> str:
    '''
    Devolve uma nova string que é como *frase*, mas com apenas a primeira letra
    em maiúscula.

    Requer que *frase* começe com uma letra.

    Exemplos
    >>> primeira_maiuscula('joao venceu.')
    'Joao venceu.'
    >>> primeira_maiuscula('A Paula é um sucesso.')
    'A paula é um sucesso.'
    '''
    return frase[0].upper() + frase[1:].lower()


if __name__ == '__main__':
    main()
