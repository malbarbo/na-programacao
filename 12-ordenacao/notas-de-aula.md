---
# vim: set spell spelllang=pt_br:
title: Ordenação
linkcolor: Black
urlcolor: Blue
# TODO: colocar imagens de heap com índices começando com 0
# TODO: adicionar ordenação por árvore
# TODO: revisar o conceito de heap (árvore completa?)
---

## Introdução

O problema de ordenação consiste em, dado uma sequência de $n$ números $\langle a_1, a_2, \ldots, a_n \rangle$, determinar uma permutação (reordenação) $\langle a_1', a_2', \ldots, a_n' \rangle$ da sequência de entrada tal que, $a_1' \leq a_2' \leq \dots \leq a_n'$.


## Projeto de algoritmos incremental

A ideia de um algoritmo incremental é: \pause

- Iniciar com a solução para um problema trivial; \pause

- Estender a solução iterativamente para um problema maior até obter a solução do problema que queremos resolver; \pause


Como projetar um algoritmo incremental para somar os elementos de um arranjo? \pause

- Começamos com a soma do arranjo vazio que é 0; \pause

- Estendemos a soma adicionando um elemento do arranjo por vez até que todos os elementos tenham sido somados.


## Ordenação incremental

Como projetar um algoritmo incremental para ordenar os elementos de um arranjo? \pause

- Iniciamos com um subarranjo vazio já ordenado; \pause

- Estendemos o subarranjo já ordenado com um elemento da parte restante por vez até que todos os elementos tenham sido selecionados. \pause

![](imagens/ordenado-resto.pdf){width=6cm} \pause

Temos que tomar duas decisões para tornar o processo concreto: \pause

- Como selecionar o próximo elemento? \pause

- Como estender o subarranjo ordenado?


## Ordenação por inserção

![](imagens/ordenado-resto.pdf){width=6cm}

Como selecionar o próximo elemento? \pause

- Pegamos o primeiro elemento do restante. \pause

Como estender o subarranjo ordenado? \pause

- Inserindo o elemento selecionado na parte ordenada. \pause

Este algoritmo é conhecido como **ordenação por inserção** (_insertion sort_).


## Ordenação por inserção

<div class="columns">
<div class="column" width="25%">
\includegraphics[trim=140pt 380pt 2000pt 50pt, clip, width=3.5cm]{imagens/Fig-2-2.pdf} \pause
\ \
</div>
<div class="column" width="25%">
\includegraphics[trim=1140pt 380pt 1000pt 50pt, clip, width=3.5cm]{imagens/Fig-2-2.pdf} \pause
</div>
<div class="column" width="25%">
\includegraphics[trim=2140pt 380pt 0pt 50pt, clip, width=3.5cm]{imagens/Fig-2-2.pdf} \pause
</div>
</div>

<div class="columns">
<div class="column" width="25%">
\includegraphics[trim=140pt 0pt 2000pt 450pt, clip, width=3.5cm]{imagens/Fig-2-2.pdf} \pause
</div>
<div class="column" width="25%">
\includegraphics[trim=1140pt 0pt 1000pt 450pt, clip, width=3.5cm]{imagens/Fig-2-2.pdf} \pause
</div>
<div class="column" width="25%">
\includegraphics[trim=2140pt 0pt 0pt 450pt, clip, width=3.5cm]{imagens/Fig-2-2.pdf}
</div>
</div>


## Ordenação por inserção

Projete uma função que implemente o algoritmo de ordenação por inserção. \pause

\scriptsize

```python

def ordena_insercao(lst: list[int]):
    '''
    Ordena *lst* em ordem não decrescente usando o algoritmo de ordenação por inserção.
    Exemplos
    >>> lst = [5, 2, 4, 6, 1, 3]
    >>> ordena_insercao(lst)
    >>> lst
    [1, 2, 3, 4, 5, 6]
    '''
```

\pause

```python
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            lst[j - 1], lst[j] = lst[j], lst[j - 1]
            j -= 1
```


## Ordenação por seleção

![](imagens/ordenado-resto.pdf){width=6cm}

Como selecionar o próximo elemento? \pause

- Pegamos o menor elemento do restante. \pause

Como estender o subarranjo ordenado? \pause

- Trocando de posição o menor elemento com o primeiro do restante. \pause

Este algoritmo é conhecido como **ordenação por seleção** (_selection sort_).


## Ordenação por seleção

Projete uma função que implemente o algoritmo de ordenação por seleção. \pause

\scriptsize

```python

def ordena_selecao(lst: list[int]):
    '''
    Ordena *lst* em ordem não decrescente usando o algoritmo de ordenação por seleção.
    Exemplos
    >>> lst = [5, 2, 4, 6, 1, 3]
    >>> ordena_selecao(lst)
    >>> lst
    [1, 2, 3, 4, 5, 6]
    '''
```

\pause

```python
    for i in range(len(lst)):
        m = i # índice do menor em lst[i:]
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[m]:
                m = j
        lst[i], lst[m] = lst[m], lst[i]
```


## Projeto de algoritmos de divisão e conquista

A ideia de um algoritmo divisão e conquista é: \pause

- Resolver o problema diretamente se ele for trivial, senão **dividir** o problema em dois ou mais subproblemas do mesmo tipo; \pause

- **Conquistar** os subproblemas resolvendo-os recursivamente; \pause

- **Combinar** as soluções dos subproblemas para obter a solução do problema original \pause


Como projetar um algoritmo de divisão e conquista para somar os elementos de um arranjo? (Note que esse algoritmo não traz nenhum vantagem, é apenas uma ilustração) \pause

- Se o arranjo for vazio, a soma é 0. Senão dividir o arranjo na metade e calcular a soma de cada metade recursivamente; \pause

- Obter a soma do arranjo somando o resultado de cada metade;


## Ordenação incremental

Como projetar um algoritmo de divisão e conquista para ordenar os elementos de um arranjo? \pause

- Se o arranjo tiver mais que um elemento, separamos os elementos em dois subarranjos; \pause

- Ordenamos cada subarranjo recursivamente; \pause

- Combinamos os dois subarranjos para obter a ordenação do arranjo inicial. \pause


Temos que tomar duas decisões para tornar o processo concreto: \pause

- Como separar os elementos em dois subarranjos? \pause

- Como combinar os dois subarranjos ordenados?


## Ordenação por intercalação

Como separar os elementos em dois subarranjos? \pause

- Dividindo o arranjo ao meio; \pause

Como combinar os dois subarranjos ordenados? \pause

- Fazendo a intercalação em ordem dos elementos dos subarranjos; \pause

Este algoritmo é conhecido como **ordenação por intercalação** (_merge sort_).


## Ordenação por intercalação

![](imagens/mergesort.pdf){width=7cm}


## Ordenação por intercalação {.t}

<div class="columns">
<div class="column" width="43%">
Projete uma função que implemente o algoritmo de ordenação por intercalação.

\pause

\scriptsize

```python

def ordena_intercalacao(lst: list[int]):
    # Se o problema não é trivial
    if len(lst) > 1:
```

\pause

```python
        # Divide em dois subproblemas
        m = len(lst) // 2
        a = lst[:m]
        b = lst[m:]
```

\pause

```python
        # Conquista recursivamente
        ordena_intercalacao(a)
        ordena_intercalacao(b)
```

\pause

```python
        # Combina as soluções
        intercala(lst, a, b)
```

\pause

</div>
<div class="column" width="52%">

Projete uma função que implemente a intercalação.

\pause

\scriptsize

```python
def intercala(lst: list[int], a: list[int], b: list[int]):
    '''
    Faz a intercalação em ordem não decrescente dos
    elementos de *a* e *b* em *lst*.
    Requer que len(lst) = len(a) + len(b).
    Requer que a e b estejam em ordem não decrescente.

    Exemplos
    >>> lst = [0, 0, 0, 0, 0, 0, 0]
    >>> intercala(lst, [1, 6], [3, 5, 6, 8, 10])
    >>> lst
    [1, 3, 5, 6, 6, 8, 10]
    >>> intercala(lst, [3, 5, 6, 8, 10], [1, 6])
    >>> lst
    [1, 3, 5, 6, 6, 8, 10]
    '''
```

</div>
</div>


## Ordenação por intercalação {.t}

<div class="columns">
<div class="column" width="43%">
Projete uma função que implemente o algoritmo de ordenação por intercalação.

\scriptsize

```python

def ordena_intercalacao(lst: list[int]):
    # Se o problema não é trivial
    if len(lst) > 1:
```

```python
        # Divide em dois subproblemas
        m = len(lst) // 2
        a = lst[:m]
        b = lst[m:]
```

```python
        # Conquista recursivamente
        ordena_intercalacao(a)
        ordena_intercalacao(b)
```

```python
        # Combina as soluções
        intercala(lst, a, b)
```

</div>
<div class="column" width="52%">

\scriptsize

```python
def intercala(lst: list[int], a: list[int], b: list[int]):
    assert len(lst) == len(a) + len(b)
    i, j, k = 0, 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            lst[k] = a[i]
            i += 1
        else:
            lst[k] = b[j]
            j += 1
        k += 1
    while i < len(a): # Copia o restante de a
        lst[k] = a[i]
        i += 1
        k += 1
    while j < len(b): # Copia o restante de b
        lst[k] = b[j]
        j += 1
        k += 1
```

</div>
</div>


## Ordenação por intercalação

<div class="columns">
<div class="column" width="43%">
Projete uma função que implemente o algoritmo de ordenação por intercalação.

\scriptsize

```python

def ordena_intercalacao(lst: list[int]):
    # Se o problema não é trivial
    if len(lst) > 1:
```

```python
        # Divide em dois subproblemas
        m = len(lst) // 2
        a = lst[:m]
        b = lst[m:]
```

```python
        # Conquista recursivamente
        ordena_intercalacao(a)
        ordena_intercalacao(b)
```

```python
        # Combina as soluções
        intercala(lst, a, b)
```

</div>
<div class="column" width="52%">

</div>
</div>


## Ordenação por intercalação

<div class="columns">
<div class="column" width="40%">
A forma mais comum de implementar a ordenação por intercalação é utilizando índices para informar o intervalo de ordenação / intercalação.

\pause

Note que nessa versão a cópia dos subarranjos geralmente é feita na função `intercala` e não em `ordena_intercala` como fizemos anteriormente.

\pause

</div>
<div class="column" width="55%">
\scriptsize

```python
def ordena_intercalacao(lst: list[int], ini: int, fim: int):
    '''
    Ordena o subarranjo lst[ini:fim] em ordem não
    decrescente.
    Requer que 0 <= i <= fim <= len(lst).
    '''
```

\pause

```python
    # Se o problema não é trivial
    if ini < fim - 1:
```

\pause

```python
        # Divide em dois subproblemas
        meio = (ini + fim) // 2
```

\pause

```python
        # Conquista recursivamente
        ordena_intercalacao(lst, ini, meio)
        ordena_intercalacao(lst, meio, fim)
```

\pause

```python
        # Combina as soluções
        intercala(lst, ini, meio, fim)
```

\pause

</div>
</div>

Projete essa versão de `intercala`.


## Divisão e conquista

No projeto de um algoritmo de divisão e conquista para ordenar um arranjo temos que tomar duas decisões: \pause

- Como separar os elementos em dois subarranjos? \pause

- Como combinar os dois subarranjos ordenados? \pause


## Divisão e conquista

Como combinar dois arranjos ordenados sem precisar passar por todos os elementos? \pause

Supondo que o arranjo de entrada `lst[0:n]`{.python} seja dividido em `lst[0:p]`{.python} e `lst[p:n]`{.python}, o que é necessário para que após a ordenação de `lst[0:p]`{.python} e `lst[p:n]`{.python} o arranjo `lst[0:n]`{.python} fique ordenado sem precisarmos fazer mais nada? \pause

Os elementos de `lst[0:p]`{.python} devem ser menores ou iguais aos elementos de `lst[p:n]`{.python}!


## Particionamento

<div class="columns">
<div class="column" width="40%">

Então, o que precisamos fazer? \pause

Projetar uma função que **particione** um arranjo em duas partes, uma com os "menores" e outra com os demais elementos ("maiores"). \pause

Para isso precisamos de um "pivô" para determinar em que parte cada elemento deve ficar. \pause

\ \

\includegraphics[trim=8cm 79cm 0cm 2.5cm, clip, width=4cm]{imagens/Fig-7-1.pdf}

\vspace{-0.5cm}

\pause \center $\downarrow$

\includegraphics[trim=8cm 0cm 0cm 82cm, clip, width=4cm]{imagens/Fig-7-1.pdf}

\pause

</div>
<div class="column" width="55%">
Faça a especificação da função que faz o particionamento de um arranjo. A função deve devolver o índice que separa as duas partes.

\pause

\scriptsize

```python

def particiona(lst: list[int], ini: int, fim: int) -> int:
    '''
    Reorganiza os elementos de lst[ini:fim] e devolve um
    índice p de maneira que os elementos de lst[ini:p]
    são menores ou iguais que lst[p:fim].

    Exemplos
    >>> lst = [2, 8, 7, 1, 3, 5, 6, 4]
    >>> particiona(lst, 0, len(lst))
    3
    >>> lst
    [2, 1, 3, 4, 8, 7, 5, 6]
    '''
```
</div>
</div>


## Ordenação por particionamento

O algoritmo de ordenação de divisão e conquista baseado na função de particionamento é chamado de **ordenação por particionamento** ou **quick sort**.

\pause

Implemente a ordenação por particionamento.


## Ordenação por partição

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def ordena_particionamento(lst: list[int],
                           ini: int,
                           fim: int):
    '''
    Ordena o subarranjo lst[ini:fim] em ordem
    não decrescente.

    Requer que 0 <= i <= fim <= len(lst).
    '''
```

\pause

```python
    # Se o problema não é trivial
    if ini < fim - 1:
```

\pause

```python
        # Divide em dois subproblemas
        p = particiona(lst, ini, fim)
```

\pause

```python
        # Conquista recursivamente
        ordena_particionamento(lst, ini, p)
        ordena_particionamento(lst, p, fim)
```

\pause

```python
        # As soluções já estão combinadas!
```

\pause

</div>
<div class="column" width="48%">

\scriptsize

```python
def ordena_intercalacao(lst: list[int],
                        ini: int,
                        fim: int):
```

\vspace{2.3cm}

```python
    # Se o problema não é trivial
    if ini < fim - 1:
```

```python
        # Divide em dois subproblemas
        meio = (ini + fim) // 2
```

```python
        # Conquista recursivamente
        ordena_intercalacao(lst, ini, meio)
        ordena_intercalacao(lst, meio, fim)
```

```python
        # Combina as soluções
        intercala(lst, ini, meio, fim)
```
</div>
</div>


## Ordenação por partição

\scriptsize

```python
def ordena_particionamento(lst: list[int],
                           ini: int,
                           fim: int):
```

```python
    # Se o problema não é trivial
    if ini < fim - 1:
```

```python
        # Divide em dois subproblemas
        p = particiona(lst, ini, fim)
```

```python
        # Conquista recursivamente
        ordena_particionamento(lst, ini, p)
        ordena_particionamento(lst, p, fim)
```

```python
        # As soluções já estão combinadas!
```


## Particionamento

<div class="columns">
<div class="column" width="40%">
Como podemos implementar a função `particiona`? \pause

Uma forma simples é usar arranjos auxiliares para armazenar as duas partições enquanto elas são construídas. \pause

</div>
<div class="column" width="56%">
\scriptsize

```python
def particiona(lst: list[int], ini: int, fim: int) -> int:
    pivo = lst[fim - 1]
    menores = []
    maiores_iguais = []
    for i in range(ini, fim - 1):
        if lst[i] < pivo:
            menores.append(lst[i])
        else:
            maiores_iguais.append(lst[i])
    # Copia os menores do que o pivo para lst
    for i in range(len(menores)):
        lst[i] = menores[i]
    # Copia o pivo para lst
    p = len(menores)
    lst[p] = pivo
    # Copias os maiores ou iguais ao pivo para lst
    for j in range(len(maiores_iguais)):
        lst[p + j + 1] = maiores_iguais[j]
    return p # Retorna o índice do pivo
```
</div>
</div>


## Particionamento in-loco

As duas formas mais comum de fazer o particionamento in-loco são: \pause

A forma sugerida por Tony Hoare, criador do quick sort, é manter dois índices, um para a partição do início do arranjo com os menores, e outro para a partição no final com os maiores. Os índices movem em direção ao meio e os elementos são trocados de lugar quando necessário. \pause

A outra forma é o particionamento de Lomuto. \pause Nesse esquema tanta a partição dos menores fica no início do arranjo e a dos maior logo em seguida.


## Particionamento de Lomuto

<div class="columns">
<div class="column" width="40%">
\includegraphics[trim=6cm 79.0cm 0cm  0.0cm, clip, width=3.5cm]{imagens/Fig-7-1.pdf} \pause
\vspace{-0.2cm}
\includegraphics[trim=6cm 69.0cm 0cm  9.8cm, clip, width=3.5cm]{imagens/Fig-7-1.pdf} \pause
\vspace{-0.2cm}
\includegraphics[trim=6cm 59.0cm 0cm 19.7cm, clip, width=3.5cm]{imagens/Fig-7-1.pdf} \pause
\vspace{-0.2cm}
\includegraphics[trim=6cm 49.0cm 0cm 29.5cm, clip, width=3.5cm]{imagens/Fig-7-1.pdf} \pause
\vspace{-0.2cm}
\includegraphics[trim=6cm 39.1cm 0cm 39.6cm, clip, width=3.5cm]{imagens/Fig-7-1.pdf} \pause
\vspace{-0.2cm}
\includegraphics[trim=6cm 29.1cm 0cm 49.4cm, clip, width=3.5cm]{imagens/Fig-7-1.pdf} \pause
\vspace{-0.2cm}
\includegraphics[trim=6cm 19.2cm 0cm 59.3cm, clip, width=3.5cm]{imagens/Fig-7-1.pdf} \pause
\vspace{-0.2cm}
\includegraphics[trim=6cm  9.3cm 0cm 69.1cm, clip, width=3.5cm]{imagens/Fig-7-1.pdf} \pause
\vspace{-0.2cm}
\includegraphics[trim=6cm  0.0cm 0cm 79.2cm, clip, width=3.5cm]{imagens/Fig-7-1.pdf} \pause
</div>
<div class="column" width="56%">
\scriptsize

```python
def particiona(lst: list[int], ini: int, fim: int) -> int:
    pivo = lst[fim - 1]
    i = ini - 1
    for j in range(ini, fim - 1):
        if lst[j] <= pivo:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[fim - 1] = lst[fim - 1], lst[i + 1]
    return i + 1
```
</div>
</div>

## Referências

Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulos 6, 7 e 8.
