---
# vim: set spell spelllang=pt_br:
# TODO: adicionar imagens mostrando a modificação da memória
title: Memória e passagem de parâmetros
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

Agora vamos explorar esse fato com mais detalhes e alguns resultados que podem parecer surpreendentes.


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

No exemplo da direita, após a execução de `y = x`, `x` e `y` referenciam a mesma célula de memória (que armazena o valor `[5, 1]`{.python}). \pause A operação `y[1] = 3`{.python} **altera** o valor armazenado na célula de memória para `[5, 3]`{.python}. \pause

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

Quando `soma1` inicia a execução, `a` e `x` referenciam a mesma célula de memória. A instrução `x = x + 1`{.python} gera um **novo valor** (`21`{.python}) que é armazenado em uma **nova célula** de memória e `x` passa a referenciar essa nova célula. `a` continua referenciado a mesma célula de memória.

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

Quando `concatena1` inicia a execução, `a` e `x` referenciam a mesma célula de memória. A instrução `x.append(1)`{.python} **altera a célula** de memória referenciada por `x` adicionando o valor `1`. `a` continua referenciado a mesma célula de memória (que foi alterada).

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


# Projeto de funções

Como projetar funções que modificam os seu argumentos? \pause

Generalizando exemplos concretos. \pause

O exemplo a seguir foi desenvolvido em sala.


# Exemplo: inverte

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def inverte(lst: list[int]) -> list[int]:
    '''
    Cria uma nova lista invertendo os elementos
    de *lst*, isto é, o último aparece como
    primeiro, o penúltimo com segundo, e assim
    por diante.
    Exemplos
    >>> inverte([8, 6, 1, 4, 5])
    [5, 4, 1, 5, 8]
    '''
    r = []
    for i in range(len(lst)):
        r.append(lst[len(lst) - i - 1])
    return r
```

</div>
<div class="column" width="48%">

\scriptsize

```python
def invertem(lst: list[int]):
    '''
    Modifica *lst* invertendo a ordem dos
    elementos, isto é, colocando o último
    elemento na segunda posição, ...
    Exemplos
    >>> x = [8, 6, 1, 4, 5]
    >>> invertem(x)
    >>> x
    [5, 4, 1, 5, 8]
    '''
    i = 0
    j = len(lst) - 1
    while i < j:
        t = lst[i]
        lst[i] = lst[j]
        lst[j] = t
        i = i + 1
        j = j - 1
```

</div>
</div>


# Exemplo: insere ordenado

Dado uma lista de números em em ordem não decrescente e um valor `v`, projete uma função que modifique a lista inserindo o valor `v` de maneira que o arranjo continue em ordem. \pause

Exemplo feito em sala.


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
    >>> insere_ordenado(lst, 5)
    >>> lst
    [5]
    >>> insere_ordenado(lst, 3)
    >>> lst
    [3, 5]
    >>> insere_ordenado(lst, 4)
    >>> lst
    [3, 4, 5]
    >>> insere_ordenado(lst, 1)
    >>> lst
    [1, 3, 4, 5]
    '''
```

\pause

</div>
<div class="column" width="48%">
\scriptsize

```python
def insere_ordenado(lst: list[int], v: int):
    lst.append(v)
    i = len(lst) - 1
    while i > 0 and lst[i - 1] > lst[i]:
        # troca lst[i] com lst[i - 1]
        t = lst[i]
        lst[i] = lst[i - 1]
        lst[i - 1] = t
        i = i - 1
```
</div>
</div>


<!--

# Especificação

\scriptsize

```cpp
// Insere v em valores de maneira que valores continue em ordem.
// Requer que valores esteja ordenado em ordem não decrescente.
void insere_ordenado(vector<int> &valores, int v) { }

examples {
    vector<int> valores = {};
    insere_ordenado(valores, 10);
    check_expect(valores, (vector<int> {10}));

    insere_ordenado(valores, 1);
    check_expect(valores, (vector<int> {1, 10}));

    insere_ordenado(valores, 2);
    check_expect(valores, (vector<int> {1, 2, 10}));

    insere_ordenado(valores, 12);
    check_expect(valores, (vector<int> {1, 2, 10, 12}));

    insere_ordenado(valores, 10);
    check_expect(valores, (vector<int> {1, 2, 10, 10, 12})); }
```


# Exemplo

<div class="columns">
<div class="column" width="48%">
\scriptsize

```cpp
vector<int> valores = {1, 2, 10, 12};
int v = 9;

valores.push_back(v);
// valores = {1, 2, 10, 12, 9}
```

\pause

```cpp
int t = valores[4];
valores[4] = valores[3];
valores[3] = t;
// valores = {1, 2, 10, 9, 12}
```

\pause

```cpp
int t = valores[3];
valores[3] = valores[2];
valores[2] = t;
// valores = {1, 2, 9, 10, 12}
```
</div>
<div class="column" width="48%">
\pause
Quais variáveis vamos precisar para o laço? \pause O índice `i`{.cpp} do elemento que está fora de ordem. \pause

Como as variáveis são inicializadas? \pause `i = valores.size() - 1`{.cpp}. \pause

Qual a condição para o laço continuar a execução? \pause `i > 0`{.cpp} e `valores[i - 1] > valores[i]`{.cpp}. \pause

O que é feito a cada iteração? O elemento na posição `i`{.cpp} é trocado de lugar com o elemento na posição `i - 1`{.cpp} e `i`{.cpp} é decrementado.
</div>
</div>


# Implementação

\scriptsize

```cpp
void insere_ordenado(vector<int> &valores, int v) {
    valores.push_back(v);
    int i = valores.size() - 1;
    while (i > 0 && valores[i - 1] > valores[i]) {
        int t = valores[i];
        valores[i] = valores[i - 1];
        valores[i - 1] = t;
        i = i - 1;
    }
}
```

\pause

Podemos melhorar? \pause

```cpp
void insere_ordenado(vector<int> &valores, int v) {
    valores.push_back(v);
    for (int i = valores.size() - 1; i > 0 && valores[i - 1] > valores[i]; i = i - 1) {
        int t = valores[i];
        valores[i] = valores[i - 1];
        valores[i - 1] = t;
    }
}
```

-->
