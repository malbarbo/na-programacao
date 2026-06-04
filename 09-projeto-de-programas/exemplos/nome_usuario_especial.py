def main() -> None:
    continuar = True
    while continuar:
        # entrada
        nome = input('Nome (vazio para parar): ')
        if nome == '':
            continuar = False
        else:
            # processamento
            usuario = nome_usuario(nome)
            # saída
            print('Usuário:', usuario)


def nome_usuario(nome: str) -> str:
    '''
    Cria um nome de usuário a partir de *nome* da seguinte forma:
    - divide *nome* em partes (separadas por  espaço)
    - junta a primeira letra de cada parte (exceto a última) e a última parte toda
    O resultado é truncado para 8 caractes  em minúsculo.
    >>> nome_usuario('   ')
    ''
    >>> nome_usuario('Maria')
    'maria'
    >>> nome_usuario('Pedro Paulo')
    'ppaulo'
    >>> nome_usuario('José Paulo da Silveira')
    'jpdsilve'
    >>> nome_usuario('Qin U Em Ca Oi Iter Sol An Do')
    'quecoisa'
    '''
    partes = nome.split()
    usuario = ''
    for i in range(len(partes) - 1):
        usuario = usuario + partes[i][0]
    if len(partes) > 0:
        usuario = usuario + partes[len(partes) - 1]
    return usuario[:8].lower()


if __name__ == '__main__':
    main()
