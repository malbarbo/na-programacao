---
# vim: set spell spelllang=pt_br:
title: Projeto de programas
---

# Introdução

Nós estamos trabalhando há bastante tempo o projeto de tipos de dados e funções isoladas (ou em pequenos conjuntos). \pause

Agora vamos ver o projeto de programas, isto é, coleções de tipos e funções para resolver um problema maior. \pause

Antes de ver as técnicas de projeto de programas, vamos ver como os programas são organizados, como eles funcionam e os tipos de programas.


# Funcionamento de um programa

As atividades realizadas por um programa podem ser divididas em: \pause

- **Entrada**: obtém os dados para processamento \pause
- **Processamento**: computa as saídas a partir das entradas \pause
- **Saída**: exibe as saídas e outras informações \pause

O processamento é o "miolo" do programa, feito por funções. \pause

A entrada e a saída são a "casca" que conecta o programa ao mundo externo.


# Composição de um programa

Um programa é composto de: \pause

- **Constantes**: nomeiam valores fixos \pause
- **Tipos de dados**: representam as informações \pause
- **Funções**: fazem o processamento e a entrada e saída de dados \pause
- **Função principal**: primeira função chamada no programa, coordena a chamada das outras funções e da entrada e saída


# Tipos de programas

Os programas se distinguem pela forma como **obtêm a entrada** e **interagem** com o mundo: \pause

- **Em lote** (não interativo): recebe todos os dados de uma vez, processa e produz a saída \pause
- **Interativo**: interage com o usuário durante a execução \pause

Vamos começar escrevendo programas interativos.


# Exemplo - nome de usuário

Projete um programa que gere nomes de usuários a partir de nomes completos. Cada nome de usuário é gerado da seguinte forma: a primeira letra de cada "parte" do nome, mais todas as letras da última parte. O nome do usuário deve ter no máximo 8 caracteres e todos devem ser minúsculos. \pause

Exemplo: "Marco Aurélio Lopes Barbosa" -> malbarbo. \pause

Como começamos? \pause

Temos duas opções: \pause

- Primeiro o projeto da função de processamento e depois a entrada e saída; ou \pause
- Primeiro a entrada e saída e depois o projeto da função de processamento

\pause

Vamos começar com o projeto da função de processamento.


# Exemplo - nome de usuário

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def nome_usuario(nome: str) -> str:
    '''
    Cria um nome de usuário a partir de *nome*
    da seguinte forma:
    - divide *nome* em partes (separadas por
      espaço)
    - junta a primeira letra de cada parte
     (exceto a última) e a última parte toda
    O resultado é truncado para 8 caracteres
    em minúsculo.
    >>> nome_usuario('Maria')
    'maria'
    >>> nome_usuario('Pedro Paulo')
    'ppaulo'
    >>> nome_usuario('José Paulo da Silveira')
    'jpdsilve'

    # alguns exemplos foram omitidos
    '''
```

\pause

</div>
<div class="column" width="48%">

\scriptsize

```python
def nome_usuario(nome: str) -> str:
    partes = nome.split()
    usuario = ''
    for i in range(len(partes) - 1):
        usuario = usuario + partes[i][0]
    if len(partes) > 0:
        usuario = usuario + partes[len(partes) - 1]
    return usuario[:8].lower()
```

\pause

\footnotesize

O `str.split` separa uma string em "palavras", descartando os espaços.

\scriptsize

```python-repl
>>> '  apenas  um  teste  '.split()
['apenas', 'um', 'teste']
```

</div>
</div>


# Exemplo - nome de usuário

Agora vamos criar a função `main`, conectando entrada, processamento e saída.

\pause

<div class="columns">
<div class="column" width="38%">

\footnotesize

```python
def main() -> None:
    # entrada
    nome = input('Nome: ')
    # processamento
    usuario = nome_usuario(nome)
    # saída
    print('Usuário:', usuario)
```

</div>
<div class="column" width="59%">

\small

Como chamar a função `main`? \pause Duas formas: \pause

- Carregar o arquivo e chamar `main` no repl. \pause
- Chamar o `main` no final do arquivo. \pause

Na segunda usamos uma condicional para que a função `main` não execute quando o arquivo é carregado como módulo:

\footnotesize

```python
if __name__ == '__main__':
    # __name__ é uma variável especial, só
    # é '__main__' quando o arquivo foi carregado
    # como principal (não módulo).
    # Quando é carregado como módulo
    # __name__ é o nome do arquivo (sem .py)
    main()
```

</div>
</div>


# Execução da linha de comando

Podemos usar o python no terminal para executar o programa. \pause

<div class="columns">
<div class="column" width="48%">
\small

Colocamos o código em um arquivo `usuarios.py`.

\scriptsize

```python
def main() -> None:
    ...


def nome_usuario(nome: str) -> str:
    ...


if __name__ == '__main__':
    main()
```

\pause
</div>
<div class="column" width="48%">

\small

E executamos com o comando python seguido do nome do arquivo:

\scriptsize

```
$ python usuarios.py
Nome: José da Silva
Usuário: jdsilva
```

\pause

\small

O programa resolve o problema proposto? \pause

Não, o problema pedia para gerar nomes de usuários a partir de nomes completos, então precisamos de uma repetição.

</div>
</div>


# Repetição de entrada

Como fazer a repetição de entrada do usuário? \pause

Temos três opções: \pause

- Perguntar quantos nomes \pause

- Perguntar após cada nome se deseja continuar \pause

- Usar uma entrada especial para sinalizar o fim


# Repetição de entrada - quantidade

<div class="columns">
<div class="column" width="58%">

\scriptsize

```python
def main() -> None:
    n = int(input('Quantos nomes? '))
    for i in range(n):
        # entrada
        nome = input('Nome ' + str(i + 1) + ': ')
        # processamento
        usuario = nome_usuario(nome)
        # saída
        print('Usuário:', usuario)
```

\pause
</div>
<div class="column" width="38%">

\small

Algum problema com esse código? \pause

Sim, se o usuário digitar algo que não é um número na quantidade, o programa falha.

Não vamos ver nessa disciplina como evitar esse problema.
</div>
</div>


# Repetição de entrada - pergunta

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def main() -> None:
    continuar = 's'
    while continuar == 's':
        # entrada
        nome = input('Nome: ')
        # processamento
        usuario = nome_usuario(nome)
        # saída
        print('Usuário:', usuario)
        # entrada
        continuar = input('Continuar (s/n)? ')
```

\pause

</div>
<div class="column" width="48%">

\small

Algum problema com esse código? \pause

Sim, se o usuário digitar qualquer coisa que não seja `'s'` o programa para. \pause Podemos resolver? Sim! \pause

\scriptsize

```python












```

</div>
</div>


# Repetição de entrada - pergunta

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def main() -> None:
    continuar = 's'
    while continuar == 's':
        # entrada
        nome = input('Nome: ')
        # processamento
        usuario = nome_usuario(nome)
        # saída
        print('Usuário:', usuario)
        # entrada
        continuar = input_sn('Continuar')
```

</div>
<div class="column" width="48%">

\small

Algum problema com esse código?

Sim, se o usuário digitar qualquer coisa que não seja `'s'` o programa para. Podemos resolver? Sim!

\scriptsize

```python
def input_sn(frase: str) -> str:
    '''
    Lê a entrada do usuário até que ele
    digite s ou n.
    Antes de cada entrada *frase* é exibido
    seguido de ' (s/n)? '
    '''
    continuar = ''
    while continuar != 's' and continuar != 'n':
        continuar = input(frase + ' (s/n)? ')
    return continuar
```

</div>
</div>


# Repetição de entrada - entrada especial

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
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
```

</div>
<div class="column" width="48%">

\small

Algum problema com esse código? \pause Não...

</div>
</div>


# Gerência de usuários

Gerar nomes de usuário é apenas uma funcionalidade, mas como proceder se o programa pode fazer mais de uma? \pause

Projete um programa que gerencie uma coleção de usuários. O programa deve permitir: adicionar novos usuários (gerando o seu nome de usuário e evitando colisão -- proponha uma forma); remover usuários existentes a partir do nome de usuário; consultar o nome a partir do nome de usuário; e listar os usuários existentes com os seus nomes. \pause

Como podemos fazer a entrada de um programa que oferece mais de uma funcionalidade? \pause

Usando um menu.


# Gerência de usuários

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
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
        # ... outros casos (2, 3, 4)
        elif opcao == '5':
            continuar = False
        else:
            print('Opção inválida')
```

</div>
<div class="column" width="48%">
\pause

Note a diferença da forma que fizemos o projeto anterior. Antes começamos com a função de processamento e depois fizemos a entrada e saída. Agora fizemos primeiro (parte) da entrada e saída, e falta fazer o processamento. \pause

Por que `cadastra` não tem retorno? \pause Porque ela tem o efeito colateral de mudar a lista de usuários. \pause

Agora é com você, termine o projeto desse programa!
</div>
</div>


# Programas em lote

Continua...
