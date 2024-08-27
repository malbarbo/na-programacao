---
# vim: set spell spelllang=pt_br:
title: Memória e passagem de parâmetros
# TODO: adicionar imagens mostrando a modificação da memória
# TODO: mostrar como as funções foram projetadas
# TODO: adicionar mais exemplos
# TODO: falar mais uma vez de valores mutáveis e imutáveis
# TODO: exemplos com estruturas
---

# Introdução

Até o momento, quais eram as nossas preocupações no projeto de programas? \pause

- Identificar o problema \pause
- Resolver o problema (com código bem escrito e testado) \pause

Agora vamos discutir outro aspecto importante no projeto de programas: \pause o uso de recursos, especificamente o uso de memória.


# Memória

A memória é um recurso compartilhado entre os diversos programas que estão em execução (processos) em um computador. \pause O sistema operacional faz a gerência de memória entre os diversos processos e garante que cada processo só tenha acesso a memória destinada a ele. \pause

Cada processo também precisa gerenciar a sua própria memória. \pause

Algumas linguagens como Python, Java e Go, fazem a gerência automática da memória. \pause Outras linguagens, como C, requerem que o programador faça a gerência da memória de forma explícita (manual).


# Gerência de memória

Cada estratégia de gerência de memória tem vantagens e desvantagem, mas o ponto principal é a facilidade de programação versus o controle. \pause Vocês vão aprender mais sobre isso ao longo do curso! \pause

A gerência de memória requer basicamente duas operações: a alocação e a desalocação de memória. \pause

O que significa alocar memória? \pause É reservar um espaço de memória para ser usada de uma determinada forma. \pause

O que significa desalocar memória? \pause É devolver para o sistema um espaço de memória que havia sido alocada previamente para que ela possa ser usada de outra forma.


# Gerência de memória em Python

Nos programas que fizemos, em que momento o Python aloca memória? \pause

- Quando um valor é criado \pause

- Quando um elemento é adicionado a uma lista e a memória reservada para a lista não é suficiente \pause


Nos programas que fizemos, em que momento o Python desaloca memória? \pause

- Quando um valor não é mais necessário


# Variáveis

Vimos anteriormente que uma variável em Python é uma referência para uma célula de memória que armazena um valor. \pause

Agora vamos explorar esse fato com mais detalhes e observar alguns resultados que podem parecer surpreendentes.


# Variáveis

<div class="columns">
<div class="column" width="48%">
Qual é o valor de `x` e `y` após a execução do seguinte trecho de código?

\footnotesize

```python
>>> x = 10
>>> y = x
>>> y = y + 3
```

\pause

```python
>>> x
10
>>> y
13
```

\pause

</div>
<div class="column" width="48%">
Qual é o valor de `x` e `y` após a execução do seguinte trecho de código?

\footnotesize

```python
>>> x = [5, 7]
>>> y = x
>>> y[1] = 3
```

\pause

```python
>>> x
[5, 3]
>>> y
[5, 3]
```

</div>
</div>


# Variáveis e apelidos

No exemplo da esquerda, após a execução de `y = x`, `x` e `y` referenciam a mesma célula de memória (que armazena o valor `10`{.python}). \pause A operação `y + 3`{.python} **cria um novo** valor que é armazenado em uma nova célula, que passa a ser referencia por `y` após `y = y + 3`. \pause

Veja [esse](https://pythontutor.com/render.html#code=x%20%3D%2010%0Ay%20%3D%20x%0Ay%20%3D%20y%20%2B%203&cumulative=false&curInstr=0&heapPrimitives=true&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false) processo no Python Tutor.

\pause

No exemplo da direita, após a execução de `y = x`, `x` e `y` referenciam a mesma célula de memória (que armazena o valor `[5, 1]`{.python}). \pause A operação `y[1] = 3`{.python} **altera** o valor armazenado na célula de memória para `[5, 3]`{.python}. \pause

Veja [esse](https://pythontutor.com/render.html#code=x%20%3D%20%5B5,%207%5D%0Ay%20%3D%20x%0Ay%5B1%5D%20%3D%203&cumulative=false&curInstr=0&heapPrimitives=true&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false) processo no Python Tutor.

\pause

Quando uma célula de memória pode ser acessada usando mais que uma variável (nome), dizemos que existem **apelidos** para a célula de memória.


# Parâmetro e apelidos

Quando uma variável é passada como parâmetro para uma função, um apelido é criado. \pause

<div class="columns">
<div class="column" width="48%">
\footnotesize

```python
>>> def soma1(x: int):
...     x = x + 1
>>> a = 20
>>> soma1(a)
>>> a
```

\pause

`20`{.python}

\pause

\small

Quando `soma1` [inicia](https://pythontutor.com/render.html#code=def%20soma1%28x%3A%20int%29%3A%0A%20%20%20%20x%20%3D%20x%20%2B%201%0A%0Aa%20%3D%2020%0Asoma1%28a%29%0Aprint%28a%29&cumulative=false&curInstr=3&heapPrimitives=true&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false) a execução, `a` e `x` referenciam a mesma célula de memória. A instrução `x = x + 1`{.python} gera um **novo valor** (`21`{.python}) que é armazenado em uma **nova célula** de memória e `x` passa a referenciar essa nova célula. `a` continua referenciado a mesma célula de memória.

\pause

</div>
<div class="column" width="48%">
\footnotesize

```python
>>> def concatena1(x: list[int]):
...     x.append(1)
>>> a = [5, 4]
>>> concatena1(a)
>>> a
```

\pause

`[5, 4, 1]`{.python}

\small

\pause

Quando `concatena1` [inicia](https://pythontutor.com/render.html#code=def%20concatena1%28x%3A%20list%5Bint%5D%29%3A%0A%20%20%20%20x.append%281%29%0A%0Aa%20%3D%20%5B5,%204%5D%0Aconcatena1%28a%29%0Aprint%28a%29&cumulative=false&curInstr=4&heapPrimitives=true&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false) a execução, `a` e `x` referenciam a mesma célula de memória. A instrução `x.append(1)`{.python} **altera a célula** de memória referenciada por `x` adicionando o valor `1`. `a` continua referenciado a mesma célula de memória (que foi alterada).

</div>
</div>


# Parâmetro e apelidos

Os apelidos podem deixar o código mais difícil de ler, mas em algumas situações eles são necessários. \pause

Suponha que queremos projetar uma função que inverta a ordem dos elementos de uma lista, isto é, coloque o último em primeiro, o penúltimo em segundo, e assim por diante. \pause

Como podemos proceder?


# Parâmetro e apelidos

Temos duas opções: \pause

1) Fazer uma função que crie uma nova lista com os elementos em ordem invertida \pause

2) Modificar a própria lista alterando a ordem dos elementos \pause

Em geral, criar uma nova lista é mais fácil, mas acarreta no uso extra de memória. Esta pode ser a única opção se tanto a lista inicial quando a lista invertida são utilizadas posteriormente. \pause

Se a lista na ordem inicial não é necessária após a chamada da função, então podemos modificar a própria lista, o que pode ser mais complicado, mas evita o uso de memória extra.


# Exemplo: inverte

Vamos ver primeiro projeto da função que cria uma nova lista.


# Exemplo: inverte

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def inverte(lst: list[int]) -> list[int]:
    '''
    Cria uma nova lista com os elementos de
    *lst* em ordem inversa, isto é, o último
    aparece como primeiro, o penúltimo com
    segundo, e assim por diante.

    Exemplos
    >>> inverte([])
    []
    >>> inverte([8, 6, 1, 4])
    [4, 1, 6, 8]
    '''
```

\pause

\footnotesize

Qual é a ideia para implementar a função? \pause Percorrer os elementos de `lst` a partir do último e adicionar em uma nova lista. \pause

Vamos escrever o código para uma lista de tamanho fixo e depois generalizar. \pause


</div>
<div class="column" width="48%">

\scriptsize

```python
    # Solução para uma lista de tamanho 4
    r = []
    r.append(lst[3])
    r.append(lst[2])
    r.append(lst[1])
    r.append(lst[0])
    return r
```

\pause

Transformando em repetição lógica: \pause

```python
    r = []
    for i in range(4):
        r.append(lst[4 - i - 1])
    return r
```

\pause

Generalizando para qualquer tamanho: \pause

```python
    r = []
    for i in range(len(lst)):
        r.append(lst[len(lst) - i - 1])
    return r
```

</div>
</div>


# Exemplo: inverte

Agora vamos projetar uma função que altera uma lista invertendo a ordem dos elementos.


# Exemplo: inverte

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def invertem(lst: list[int]):
    '''
    Inverte a ordem dos elementos de *lst*,
    isto é, colocando o último elemento na
    primeira posção, o penúltimo na segunda
    posição, e assim por diante.

    Exemplos
    >>> x = []
    >>> invertem(x)
    >>> x
    []
    >>> x = [8, 6, 1, 4, 5]
    >>> invertem(x)
    >>> x
    [5, 4, 1, 6, 8]
    '''
```

\pause


</div>
<div class="column" width="48%">

\small

De que forma a especificação dessa função é diferente das demais? \pause

Não tem tipo de saída. \pause Por que? \pause A função não vai produzir uma saída e sim o efeito colateral de modificar a lista. \pause

O propósito enfatiza que a lista é modificada. \pause

Os exemplos são especificados em três partes: inicialização dos parâmetros, chamada da função e verificação do efeito.
</div>
</div>


# Exemplo: inverte

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def invertem(lst: list[int]):
    '''
    Inverte a ordem dos elementos de *lst*,
    isto é, colocando o último elemento na
    primeira posção, o penúltimo na segunda
    posição, e assim por diante.

    Exemplos
    >>> x = [8, 6, 1, 4, 5]
    >>> invertem(x)
    >>> x
    [5, 4, 1, 6, 8]
    '''
```

\footnotesize

Qual é a ideia para implementar a função? \pause Troca o primeiro com o último, o segundo com o penúltimo e assim por diante. \pause

Vamos escrever o código para uma lista de tamanho fixo e depois generalizar. \pause

</div>
<div class="column" width="48%">

\scriptsize

```python
    # Vamos escrever a solução para
    # uma lista de tamanho 5
```

\pause

```python
    # troca lst[0] <-> lst[4]
    # lst = [8, 6, 1, 4, 5] -> [5, 6, 1, 4, 8]
```

\pause

```python
    t = lst[0]
    lst[0] = lst[4]
    lst[4] = t
```

\pause

```python
    # troca lst[1] <-> lst[3]
    # [5, 6, 1, 4, 8] -> [5, 4, 1, 6, 8]
```

\pause

```python
    t = lst[1]
    lst[1] = lst[3]
    lst[3] = t
```

\pause

Transformando em repetição lógica:

\scriptsize

```python
    for i in range(2):
        # troca lst[i] <-> lst[5 - i - 1]
```

</div>
</div>


# Exemplo: inverte

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def invertem(lst: list[int]):
    '''
    Inverte a ordem dos elementos de *lst*,
    isto é, colocando o último elemento na
    primeira posção, o penúltimo na segunda
    posição, e assim por diante.

    Exemplos
    >>> x = [8, 6, 1, 4, 5]
    >>> invertem(x)
    >>> x
    [5, 4, 1, 6, 8]
    '''
```

\footnotesize

Qual é a ideia para implementar a função? Troca o primeiro com o último, o segundo com o penúltimo e assim por diante.

Vamos escrever o código para uma lista de tamanho fixo e depois generalizar.

</div>
<div class="column" width="48%">

\small

Transformando em repetição lógica:

\scriptsize

```python
    for i in range(2):
        # troca lst[i] <-> lst[5 - i - 1]
```

\pause

```python
        t = lst[i]
        lst[i] = lst[5 - i - 1]
        lst[5 - i - 1] = t
```

\pause

\small

Generalizando para qualquer tamanho: \pause

\scriptsize

```python
    for i in range(len(lst) // 2):
        # troca lst[i] <-> lst[len(lst) - i - 1]
        t = lst[i]
        lst[i] = lst[len(lst) - i - 1]
        lst[len(lst) - i - 1] = t
```

</div>
</div>


# Exemplo: insere ordenado

Dado uma lista de números em em ordem não decrescente e um valor `v`, projete uma função que modifique a lista inserindo o valor `v` de maneira que o arranjo continue em ordem.


# Exemplo: insere ordenado

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def insere_ordenado(lst: list[int], v: int):
    '''
    Insere *v* em *lst* de maneira que *lst*
    permaneça em ordem não decrescente. Requer
    que *lst* esteja em ordem não decrescente.
    Exemplos
    >>> lst = []
    >>> insere_ordenado(lst, 7)
    >>> lst
    [7]
    >>> insere_ordenado(lst, 3)
    >>> lst
    [3, 7]
    >>> insere_ordenado(lst, 5)
    >>> lst
    [3, 5, 7]
    >>> insere_ordenado(lst, 4)
    >>> lst
    [3, 4, 5, 7]
    '''
```

\pause

</div>
<div class="column" width="48%">

Qual é a ideia para implementar a função? \pause Colocar `v` no final de `lst` e ir trocando ele de lugar com o antecessor até chegar no "lugar certo". \pause

Vamos escrever o código para uma lista de tamanho fixo e depois generalizar.

</div>
</div>


# Exemplo: insere ordenado

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def insere_ordenado(lst: list[int], v: int):
    '''
    Insere *v* em *lst* de maneira que *lst*
    permaneça em ordem não decrescente. Requer
    que *lst* esteja em ordem não decrescente.
    Exemplos
    >>> lst = []
    >>> insere_ordenado(lst, 7)
    >>> lst
    [7]
    >>> insere_ordenado(lst, 3)
    >>> lst
    [3, 7]
    >>> insere_ordenado(lst, 5)
    >>> lst
    [3, 5, 7]
    >>> insere_ordenado(lst, 4)
    >>> lst
    [3, 4, 5, 7]
    '''
```

</div>
<div class="column" width="48%">

\scriptsize

```python
    # v = 4
    # lst = [3, 5, 7] -> [3, 5, 7, 4]
```

\pause

```python
    lst.append(v)
```

\pause

```python
    # lst[2] > lst[3], então troca lst[3] <-> lst[2]
    # [3, 5, 7, 4] -> [3, 5, 4, 7]
```

\pause

```python
    t = lst[3]
    lst[3] = lst[2]
    lst[2] = t
```

\pause

```python
    # lst[1] > lst[2], então troca lst[2] <-> lst[1]
    # [3, 5, 4, 7] -> [3, 4, 5, 7]
```

\pause

```python
    t = lst[2]
    lst[2] = lst[1]
    lst[1] = t
```

\pause

```python
    # lst[0] < lst[1], ou seja,
    # v está na posição "certa", então para
    # [3, 4, 5, 7]
```

</div>
</div>


# Exemplo: insere ordenado

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def insere_ordenado(lst: list[int], v: int):
    '''
    Insere *v* em *lst* de maneira que *lst*
    permaneça em ordem não decrescente. Requer
    que *lst* esteja em ordem não decrescente.
    Exemplos
    >>> lst = []
    >>> insere_ordenado(lst, 7)
    >>> lst
    [7]
    >>> insere_ordenado(lst, 3)
    >>> lst
    [3, 7]
    >>> insere_ordenado(lst, 5)
    >>> lst
    [3, 5, 7]
    >>> insere_ordenado(lst, 4)
    >>> lst
    [3, 4, 5, 7]
    '''
```

</div>
<div class="column" width="48%">

Transformando em repetição lógica:

\scriptsize

```python
    lst.append(v)
    i = 3
    while ...:
        # troca lst[i] <-> lst[i - 1]
        ...
        i = i - 1
```

\pause

\normalsize

Completando

\scriptsize

```python
    lst.append(v)
    i = 3
    while i > 0 and lst[i - 1] > lst[i]:
        # troca lst[i] <-> lst[i - 1]
        t = lst[i]
        lst[i] = lst[i - 1]
        lst[i - 1] = t
        i = i - 1
```

</div>
</div>


# Exemplo: insere ordenado

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def insere_ordenado(lst: list[int], v: int):
    '''
    Insere *v* em *lst* de maneira que *lst*
    permaneça em ordem não decrescente. Requer
    que *lst* esteja em ordem não decrescente.
    Exemplos
    >>> lst = []
    >>> insere_ordenado(lst, 7)
    >>> lst
    [7]
    >>> insere_ordenado(lst, 3)
    >>> lst
    [3, 7]
    >>> insere_ordenado(lst, 5)
    >>> lst
    [3, 5, 7]
    >>> insere_ordenado(lst, 4)
    >>> lst
    [3, 4, 5, 7]
    '''
```

</div>
<div class="column" width="48%">

Generalizando para qualquer tamanho:

\scriptsize

```python
def insere_ordenado(lst: list[int], v: int):
    lst.append(v)
    i = len(lst) - 1
    while i > 0 and lst[i - 1] > lst[i]:
        # troca lst[i] <-> lst[i - 1]
        t = lst[i]
        lst[i] = lst[i - 1]
        lst[i - 1] = t
        i = i - 1
```
</div>
</div>


# Revisão

Em Python as variáveis são referências para células de memória que armazenam valores. \pause

Apelidos são variáveis que referenciam a mesma célula de memória. \pause

Quando atribuímos uma variável para outra e quando passamos uma variável como parâmetro para uma função, estamos criando um apelido. \pause

Usamos apelidos (passagem de parâmetro por referência) no projeto de funções que alteram os argumentos (efeito colateral).


# Revisão

Escrevemos o propósito das funções que alteram os argumentos destacando que os argumentos são alterados. \pause

Os exemplos são especificados em três partes: inicialização dos parâmetros, chamada da função e verificação da modificação (efeito colateral). \pause

Na implementação começamos com uma ideia, depois iniciamos a implementação com repetição física de código que concretiza a ideia para uma lista de tamanho fixo, depois transformamos a repetição física em repetição lógica e por fim generalizamos a implementação para listas de qualquer tamanho.
