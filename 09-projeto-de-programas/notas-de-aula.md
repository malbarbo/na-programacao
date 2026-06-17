---
# vim: set spell spelllang=pt_br:
title: Projeto de programas
---

# Introdução

Nós estamos trabalhando há bastante tempo o projeto de tipos de dados e funções isoladas (ou em pequenos conjuntos). \pause

Agora vamos ver o projeto de programas, isto é, coleções de tipos e funções para resolver um problema maior, juntamente com uma interface para o usuário. \pause

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

- **Em lote** (não interativo): recebe todos os dados do usuário de uma vez, processa e produz a saída \pause
- **Interativo**: interage com o usuário durante a execução para obter os dados de entrada \pause

Vamos começar projetando programas interativos.


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

\pause

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

Colocamos o código em um arquivo `nome_usuario.py`.

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
$ python nome_usuario.py
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

Sim, se o usuário digitar algo que não é um número na quantidade, o programa falha. \pause

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

Sim, se o usuário digitar qualquer coisa que não seja `'s'`{.python} o programa para. \pause Podemos resolver? \pause Sim! \pause

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
        if nome != '':
            # processamento
            usuario = nome_usuario(nome)
            # saída
            print('Usuário:', usuario)
        else:
            continuar = False
```

</div>
<div class="column" width="48%">

\small

Algum problema com esse código? \pause Não... \pause mas \pause

Já existe uma forma do usuário sinalizar que a entrada acabou (eof - _end of file_): \pause

- Linux / macOS: `ctrl + d` \pause
- Windows: `ctrl + z` seguido de `enter` \pause

O que a função `input`{.python} produz nesses casos? \pause Nada, a função crasha (lança uma exceção). \pause

Para identificar eof sem crashar, podemos usar a função `sys.stdin.readline`{.python}.

</div>
</div>


# Repetição de entrada - entrada especial

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
import sys

def main() -> None:
    continuar = True
    while continuar:
        # entrada
        sys.stdout.write('Nome: ')
        nome = sys.stdin.readline()
        # remove brancos no início e fim
        nome = nome.strip()
        if nome != '':
            # processamento
            usuario = nome_usuario(nome)
            # saída
            print('Usuário:', usuario)
        else:
            continuar = False
```

</div>
<div class="column" width="48%">

\small

Diferenças entre `input`{.python} e `sys.stdin.readline`{.python}: \pause

- `input`{.python}: exibe uma mensagem, lê e devolve a entrada sem `'\n'`{.python} (marca de fim de linha / enter do usuário). Crasha quando lê eof. \pause

- `sys.stdin.readline`{.python}: lê e devolve a entrada com `'\n'`{.python}, devolve `''`{.python} quando lê eof.

</div>
</div>


# Gerência de usuários

Gerar nomes de usuário é apenas uma funcionalidade, mas como proceder se o programa pode fazer mais de uma? \pause

Projete um programa que gerencie uma coleção de usuários. O programa deve permitir: adicionar novos usuários (gerando o seu nome de usuário e evitando colisão -- proponha uma forma); remover usuários existentes a partir do nome de usuário; consultar o nome a partir do nome de usuário; e listar os usuários existentes com os seus nomes. \pause

Como podemos fazer a entrada de um programa que oferece mais de uma funcionalidade? \pause

Usando um menu.


# Gerência de usuários

<div class="columns">
<div class="column" width="41%">

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
<div class="column" width="58%">
\pause

\small

Por que `cadastra` não tem retorno? \pause Porque ela tem o efeito colateral de mudar a lista de usuários. \pause

Note a diferença da forma que fizemos o projeto anterior. Antes começamos com a função de processamento e depois fizemos a entrada e saída. Agora fizemos primeiro (parte) da entrada e saída e depois temos que fazer as funções de processamento. \pause

Durante a implementação de `cadastra` (e outras funções), podemos identificar a necessidade de criar novas funções, e o mesmo pode acontecer para essas novas funções, e assim por diante!

</div>
</div>


# Gerência de usuários

<div class="columns">
<div class="column" width="41%">

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
<div class="column" width="58%">
\small

Então, começamos de cima (a casca de entrada e saída) e vamos fazendo o refinamento sucessivo, isto é, identificando e projetando novas funções, até chegar em funções folhas (que não dependem de outras funções). \pause

Essa abordagem é de cima para baixo (em inglês, _top down_). \pause

Existe uma abordagem de baixo para cima (_bottom up_)? \pause Sim, mas ela é usada em situações específicas, quando já conhecemos de antemão as funções folhas. \pause

Agora é com você, termine o projeto desse programa usando a abordagem de cima para baixo.
</div>
</div>


# Programas em lote

Como projetar programas em lote (não interativos)? \pause

Como um programa em lote obtém os dados de entrada? \pause

Antes de responder, vamos conversar sobre entrada e saída padrão.


# Entrada e saída padrão

Em um programa a origem das entradas e o destino das saídas podem ser diversos. \pause Em geral, cada destino/origem de dados tem um identificador numérico chamado de `fd` (_file descriptor_). \pause

A origem padrão dos dados de entrada é chamada de **entrada padrão** -- `fd 0` (em inglês _standard input_ ou _stdin_). \pause Normalmente o teclado. \pause A entrada padrão é a origem dos dados da função `input`{.python} e da função `sys.stdin.readline`{.python}.\pause

O destino padrão dos dados de saída é chamado de **saída padrão** -- `fd 1` (em inglês _standard output_ ou _stdout_). \pause Normalmente a janela do terminal. \pause A saída padrão é o destino dos dados da função `print`{.python} e da função `sys.stdout.write`{.python}. \pause

O destino padrão dos dados de erro é chamado de **saída de erro padrão** -- `fd 2` (em inglês _standard error_ ou _stderr_). \pause Normalmente a janela do terminal. \pause A saída de erro padrão é o destino dos dados da função `sys.stderr.write`{.python}.


# Redirecionamento

Como diferenciamos a saída padrão e a saída de erro padrão se normalmente são as mesmas? \pause Não diferenciamos visualmente! \pause

<div class="columns">
<div class="column" width="48%">
\scriptsize

Arquivo `saida.py`

```python
import sys

# mesmo que sys.stdout.write("tudo certo\n")
print("tudo certo")

# mesmo que sys.stderr.write("deu ruim\n")
print("deu ruim", file=sys.stderr)
```

\pause

</div>
<div class="column" width="48%">
\scriptsize

Execução

```
$ python saida.py
tudo certo
deu ruim
```

\pause

Mas podemos redirecionar uma das saídas para outro destino, por exemplo, um arquivo.

\pause

Na chamada abaixo a saída de erro padrão (`fd 2`) é redirecionada para o arquivo `erro.txt` (`cat` mostra o conteúdo do arquivo):

```
$ python saida.py 2> erro.txt
tudo certo
$ cat erro.txt
deu ruim
```

</div>
</div>

# Redirecionamento

Podemos também redirecionar a entrada padrão? \pause Sim! \pause

<div class="columns">
<div class="column" width="48%">
\scriptsize

Arquivo `echo.py`

```python
import sys

def main() -> None:
    continuar = True
    while continuar:
        linha = sys.stdin.readline()
        if linha != '':
            sys.stdout.write(linha)
        else:
            continuar = False
```

\pause

Arquivo `teste.txt`

```
Apenas um
teste
```

\pause

</div>
<div class="column" width="48%">
\scriptsize

Sem redirecionamento, lê uma linha do usuário, escreve a mesma linha.

```
$ python echo.py
Apenas um
Apenas um
teste
teste
```

\pause

Com redirecionamento, lê cada linha do arquivo `teste.txt` e escreve cada linha.

```
$ python echo.py < teste.txt
Apenas um
teste
```

</div>
</div>


# Programas em lote

Como um programa em lote obtém os dados de entrada? \pause

- Da entrada padrão redirecionada \pause (já vimos) \pause
- Da linha de comando \pause (vamos ver agora) \pause
- De entradas fixas no programa (nomes de arquivos, endereços de internet, etc) \pause (não veremos)


# Linha de comando

Os argumentos passados na linha de comando são armazenados na lista `sys.argv`{.python}, onde `argv[0]`{.python} armazena o nome do programa. \pause

Projete um programa `ola.py` que funcione da seguinte forma:

<div class="columns">
<div class="column" width="48%">

\scriptsize

```
$ python ola.py
Olá mundo!
```

\pause

```
$ python ola.py José "Ana Maria"
Olá José!
Olá Ana Maria!
```

\pause

</div>
<div class="column" width="48%">

\scriptsize

```python
import sys

def main() -> None:
    if len(sys.argv) <= 1:
        print(ola('mundo'))
    else:
        for nome in sys.argv[1:]:
            print(ola(nome))

def ola(nome: str) -> str:
    return 'Olá ' + nome + '!'
```

</div>
</div>


# Argumentos, entrada padrão ou arquivo?

Vimos várias formas de um programa em lote obter os dados de entrada. \pause Quanto cada uma é mais adequada? \pause

Os argumentos da linha de comando controlam o *comportamento* do programa: quais opções usar, em qual modo executar e, muitas vezes, de onde ler os dados. \pause São poucos e já conhecidos na hora de chamar o programa. \pause

Os dados a processar, quando são muitos, não cabem nos argumentos: vêm da entrada padrão ou de arquivos.


# Argumentos, entrada padrão ou arquivo?

E entre a entrada padrão e um arquivo, qual usar? \pause

Usamos a entrada padrão quando o programa processa um fluxo de dados e queremos poder trocar a origem sem mudar o código. \pause

\scriptsize

```
$ python estatisticas.py < temperaturas.txt
```

\normalsize
\pause

Informamos o **nome de um arquivo** quando o programa precisa do nome em si, por exemplo para citá-lo em mensagens ou para processar vários arquivos. \pause

\scriptsize

```
$ python estatisticas.py temperaturas.txt
```

# Projeto de programas não interativos

Como projetar programas em lote (não interativos)? \pause

Usando a abordagem _top-down_. \pause

Definimos as funcionalidades, como elas são chamadas pela linha de comando, escrevemos o código que analisa os argumentos e definimos quais funções de processamento será necessárias.


# Revisão

Em quais atividades podemos dividir o funcionamento de um programa? \pause

- Entrada, processamento e saída. \pause

Quais são os dois tipos de programa quanto à obtenção da entrada? \pause

- Em lote (não interativo) e interativo. \pause

Cite três formas de repetir a entrada em um programa interativo. \pause

- Perguntar a quantidade; perguntar a cada item se deseja continuar; usar uma entrada especial (vazia ou eof) para sinalizar o fim.


# Revisão

O que acontece quando `input`{.python} encontra o eof? \pause

- A função crasha (lança uma exceção). Já `sys.stdin.readline`{.python} devolve `''`{.python}. \pause

O que é a abordagem de cima para baixo (_top down_)? \pause

- Começamos pela casca de entrada e saída e vamos refinando, identificando e projetando novas funções até chegar nas funções folhas.


# Revisão

Quais são as três saídas/origens padrão e seus `fd`? \pause

- Entrada padrão (`fd 0`), saída padrão (`fd 1`) e saída de erro padrão (`fd 2`). \pause

Para que servem os argumentos da linha de comando e de onde vêm os dados? \pause

- Os argumentos controlam o comportamento (opções, qual fonte usar); os dados a processar vêm da entrada padrão ou de um arquivo. \pause

Onde ficam os argumentos no programa? \pause

- Na lista `sys.argv`{.python}, sendo `sys.argv[0]`{.python} o nome do programa.
