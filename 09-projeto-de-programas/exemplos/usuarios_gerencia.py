# Esqueleto do gerenciador de usuários (exercício).
#
# O main com o menu já está pronto; falta projetar as funções de
# processamento (cadastra, remove, consulta e lista).

from dataclasses import dataclass


@dataclass
class Usuario:
    '''Um usuário, com o *nome* completo e o *nome_usuario* gerado.'''
    nome: str
    nome_usuario: str


def main() -> None:
    usuarios: list[Usuario] = []
    continuar = True
    while continuar:
        print('1) Cadastrar')
        print('2) Remover')
        print('3) Consultar')
        print('4) Listar')
        print('5) Sair')
        opcao = input('Opção? ')
        if opcao == '1':
            print('-- Cadastra --')
            nome = input('Nome: ')
            cadastra(usuarios, nome)
        elif opcao == '2':
            print('-- Remove --')
            usuario = input('Usuário: ')
            remove(usuarios, usuario)
        elif opcao == '3':
            print('-- Consulta --')
            usuario = input('Usuário: ')
            consulta(usuarios, usuario)
        elif opcao == '4':
            print('-- Lista --')
            lista(usuarios)
        elif opcao == '5':
            continuar = False
        else:
            print('Opção inválida')


def cadastra(usuarios: list[Usuario], nome: str) -> None:
    '''
    Cadastra em *usuarios* um novo usuário com o *nome* informado, gerando o
    seu nome de usuário e evitando colisão com os já existentes.
    '''
    ...  # TODO: implementar


def remove(usuarios: list[Usuario], usuario: str) -> None:
    '''
    Remove de *usuarios* o usuário com nome de usuário *usuario*, se existir.
    '''
    ...  # TODO: implementar


def consulta(usuarios: list[Usuario], usuario: str) -> None:
    '''
    Exibe o nome completo do usuário com nome de usuário *usuario*, se existir.
    '''
    ...  # TODO: implementar


def lista(usuarios: list[Usuario]) -> None:
    '''
    Exibe todos os usuários de *usuarios* com os seus nomes.
    '''
    ...  # TODO: implementar


def nome_usuario(nome: str) -> str:
    '''
    Cria um nome de usuário a partir de *nome* da seguinte forma:
    - divide *nome* em partes (separadas por espaço)
    - junta a primeira letra de cada parte (exceto a última) e a última parte toda
    O resultado é truncado para 8 caracteres em minúsculo.
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
