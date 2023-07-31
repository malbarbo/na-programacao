def main():
    print('Este programa verifica se o primeiro nome de uma pessoa é Paula e se o sobrenome é Silva.')

    # Entrada
    nome: str = input('Digite um nome composto (sem espaço no início e fim): ')

    # Processamento
    eh_paula = nome_eh_paula(nome)
    eh_silva = sobrenome_eh_silva(nome)

    # Saída
    print('O primeiro nome é Paula?', eh_paula)
    print('O primeiro sobrenome é Silva?', eh_silva)


def nome_eh_paula(nome_completo: str) -> bool:
    '''
    Produz True se o primeiro nome de *nome_completo* é Paula, False caso contrário.

    Requer que *nome_completo* não começe e nem termine com espaços e que
    contenha pelo menos um espaço em branco.

    Exemplos
    >>> nome_eh_paula('Paula da Silva')
    True
    >>> nome_eh_paula('Paulah de Maringá')
    False
    >>> nome_eh_paula('J B')
    False
    '''
    return len(nome_completo) > 6 and nome_completo[:6] == 'Paula '


def sobrenome_eh_silva(nome_completo: str) -> bool:
    '''
    Produz True se o último nome (sobrenome) de *nome_completo* é Silva, False
    caso contrário.

    Requer que *nome_completo* não começe e nem termine com espaços e que
    contenha pelo menos um espaço em branco.

    Exemplos
    >>> nome_eh_paula('Paula da Silva')
    True
    >>> nome_eh_paula('João SaSilva')
    False
    >>> nome_eh_paula('J B')
    False
    '''
    return len(nome_completo) > 6 and nome_completo[-6:] == ' Silva'


if __name__ == '__main__':
    main()
