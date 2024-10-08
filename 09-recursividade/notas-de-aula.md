---
# vim: set spell spelllang=pt_br:
title: Recursividade
# TODO: mostrar em linguagem natural um procedimento para somar os números
#       naturais, semelhante a verificação se 4 é natural.
# TODO: quando falar de diminuição e conquista já dar um exemplo.
---

# Introdução

Nós vimos como a definição adequada de tipos de dados é importante no projeto de programas. \pause

Agora vamos explorar como a forma da definição do tipo de dado pode nos ajudar a escrever o corpo das funções.


# Número natural

Considere a seguinte definição de número natural: \pause

- $0$ é um número natural; \pause
- Se $n$ é um número natural, então $n + 1$ é um número natural. \pause

O que esta definição tem de diferente? \pause

No segundo caso, um número natural é definido em termos de outro número natural! \pause Como isso é possível!?


# Definições recursivas

Como é possível algo ser definido em termos de si mesmo? \pause

É possível porque um algo maior está sendo definido em termos do mesmo tipo de algo, mas menor. \pause Como não é possível diminuir algo infinitamente, em algum momento teremos um algo básico, que não é composto de outro algo. \pause

Esse tipo de definição é muito utilizado na computação e matemática.


# Definições recursivas

Uma **definição recursiva** (ou definição indutiva) e uma definição que é feita em termos de si mesma. \pause

Para estar bem formada, uma definição recursiva precisa de:\pause

- Pelo menos um caso base (que não depende da própria definição); \pause
- Pelo menos um caso com autorreferência (que depende da própria definição para elementos "menores"). \pause

A partir do(s) caso(s) base, os outros elementos são definidos de forma indutiva pelos casos com autorreferência.


# Definições recursivas

Definição de número natural:

- $0$ é um número natural;
- Se $n$ é um número natural, então $n + 1$ é um número natural.

O número 4 é natural? \pause Vamos verificar \pause

- Como 4 não é zero, para ele ser natural, o 3 tem que ser natural; \pause
- Como 3 não é zero, para ele ser natural, o 2 tem que ser natural; \pause
- Como 2 não é zero, pare ele ser natural, o 1 tem que ser natural; \pause
- Como 1 não é zero, pare ele ser natural, o 0 tem que ser natural; \pause
- Por definição, 0 é natural. \pause

Portanto, o 4 é natural. \pause Note que foi preciso decompor o 4 até chegar no caso base.


# Funções recursivas

Assim como temos definições recursivas, também temos funções recursivas. \pause

Uma **função recursiva** é aquela que chama a si mesmo. \pause

Assim como para definições recursivas, para estar bem formada, uma função recursiva precisa de: \pause

- Pelo menos um caso base (o valor da função é calculado diretamente); \pause
- Pelo menos um caso com chamada recursiva (depende do valor da função para entradas menores).


# Projeto de funções recursivas

Como projetar funções recursivas? \pause

Existem várias técnicas de projeto de funções recursivas, nós vamos explorar uma delas, chamada de **diminuição e conquista**. \pause

A ideia é diminuir o problema inicial gerando um novo problema, conquistar o novo problema -- diretamente ou recursivamente -- e estender a solução do novo problema para o problema inicial. \pause

No início, para diminuir o problema inicial, nós vamos explorar a relação entre autorreferência na definição do tipo de dado e a chamada recursiva na função que processa o tipo de dado.


# Exemplo: soma naturais

Projete uma função recursiva que some todos os números naturais menores ou iguais que um determinado $n$.


# Exemplo: soma naturais

<div class="columns">
<div class="column" width="45%">
\scriptsize

```python
def soma_naturais(n: int) -> int:
    '''
    Soma todos os número naturais menores
    ou iguais que *n*.
    Requer que n >= 0.
    Exemplos
    >>> soma_naturais(0)
    0
    >>> soma_naturais(1)
    1
    >>> soma_naturais(2)
    3
    >>> soma_naturais(3)
    6
    >>> soma_naturais(4)
    10
    '''
    return 0
```
</div>
<div class="column" width="55%">
\pause

\small
Como a definição de número natural tem dois casos, vamos começar a implementação da função com dois casos. \pause

\scriptsize

```python
if n == 0:
    ...
else:
    n ...
```

\pause
\small
Como o segundo caso da definição de número natural tem uma autorreferência, vamos colocar uma chamada recursiva no segundo caso da função. \pause

\scriptsize

```python
if n == 0:
    ...
else:
    n ... soma_naturais(n - 1)
```

</div>
</div>


# Exemplo: soma naturais

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def soma_naturais(n: int) -> int:
    '''
    Soma todos os número naturais menores
    ou iguais que *n*.
    Requer que n >= 0.
    Exemplos
    >>> soma_naturais(0)
    0
    >>> soma_naturais(1)
    1
    >>> soma_naturais(2)
    3
    >>> soma_naturais(3)
    6
    >>> soma_naturais(4)
    10
    '''
```

</div>
<div class="column" width="48%">
\scriptsize

```python
def soma_naturais(n: int) -> int:
    if n == 0:
        # Qual é a soma dos naturais
        # até n == 0?
        soma = ...
    else:
        # Tendo a soma dos naturais
        # até n - 1 e o natural n,
        # como obter a soma dos
        # naturais até n?
        soma = n ... soma_naturais(n - 1)
    return soma
```
</div>
</div>


# Exemplo: soma naturais

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def soma_naturais(n: int) -> int:
    '''
    Soma todos os número naturais menores
    ou iguais que *n*.
    Requer que n >= 0.
    Exemplos
    >>> soma_naturais(0)
    0
    >>> soma_naturais(1)
    1
    >>> soma_naturais(2)
    3
    >>> soma_naturais(3)
    6
    >>> soma_naturais(4)
    10
    '''
```

</div>
<div class="column" width="48%">
\scriptsize

```python
def soma_naturais(n: int) -> int:
    if n == 0:
        # Qual é a soma dos naturais
        # até n == 0?
        soma = 0
    else:
        # Tendo a soma dos naturais
        # até n - 1 e o natural n,
        # como obter a soma dos
        # naturais até n?
        soma = n + soma_naturais(n - 1)
    return soma
```
</div>
</div>


# Exemplo: exponencial

Projete uma função recursiva que receba como entrada um número $a \not = 0$ e um número natural $n$ e calcule o valor $a^n$.


# Exemplo: exponencial

<div class="columns">
<div class="column" width="45%">
\scriptsize

```python
def potencia(a: float, n: int) -> float:
    '''
    Calcula *a* elevado a *n*.
    Requer que a != 0 e n >= 0.
    Exemplos
    >>> potencia(2.0, 0)
    1.0
    >>> potencia(2.0, 1)
    2.0
    >>> potencia(2.0, 2)
    4.0
    >>> potencia(2.0, 3)
    8.0
    >>> potencia(3.0, 3)
    27.0
    >>> potencia(3.0, 4)
    81.0
    '''
    return 0.0
```

</div>
<div class="column" width="52%">
\pause

\small
Como a definição de número natural tem dois casos, vamos começar a implementação da função com dois casos. \pause

\scriptsize

```python
if n == 0:
    a ...
else:
    a ... n ...

```

\pause
\small
Como o segundo caso da definição de número natural tem uma autorreferência, vamos colocar uma chamada recursiva no segundo caso da função. \pause

\scriptsize

```python
if n == 0:
    a ...
else:
    a ... n ... potencia(a, n - 1)
```

</div>
</div>


# Exemplo: exponencial

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def potencia(a: float, n: int) -> float:
    '''
    Calcula *a* elevado a *n*.
    Requer que a != 0 e n >= 0.
    Exemplos
    >>> potencia(2.0, 0)
    1.0
    >>> potencia(2.0, 1)
    2.0
    >>> potencia(2.0, 2)
    4.0
    >>> potencia(2.0, 3)
    8.0
    >>> potencia(3.0, 3)
    27.0
    >>> potencia(3.0, 4)
    81.0
    '''
```

</div>
<div class="column" width="48%">
\scriptsize

```python
def potencia(a: float, n: int) -> float:
    if n == 0:
        # Qual é o valor de a^n
        # quando n == 0?
        an = a ...
    else:
        # Tendo a potência a^(n - 1),
        # o valor de a e n, como
        # calcular a^n?
        an = a ... n ... potencia(a, n - 1)
    return an
```
</div>
</div>


# Exemplo: exponencial

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def potencia(a: float, n: int) -> float:
    '''
    Calcula *a* elevado a *n*.
    Requer que a != 0 e n >= 0.
    Exemplos
    >>> potencia(2.0, 0)
    1.0
    >>> potencia(2.0, 1)
    2.0
    >>> potencia(2.0, 2)
    4.0
    >>> potencia(2.0, 3)
    8.0
    >>> potencia(3.0, 3)
    27.0
    >>> potencia(3.0, 4)
    81.0
    '''
```

</div>
<div class="column" width="48%">
\scriptsize

```python
def potencia(a: float, n: int) -> float:
    if n == 0:
        # Qual é o valor de a^n
        # quando n == 0?
        an = 1.0
    else:
        # Tendo a potência a^(n - 1),
        # o valor de a e n, como
        # calcular a^n?
        an = a * potencia(a, n - 1)
    return an
```
</div>
</div>


# Aspectos importantes no projeto de funções recursivas

Quando estamos projetando funções recursivas, temos que considerar dois aspectos: \pause

- A chamada recursiva deve ser feita para uma **entrada "menor"**, dessa forma, temos a certeza que o caso base será alcançado e a função terminará; \pause

- Devemos **confiar na chamada recursiva**, isto é, que ela produz a resposta correta, e nos preocuparmos apenas em como utilizar essa resposta para calcular o resultado da função.


# Funções recursivas com arranjos

Podemos projetar funções recursivas que operam em arranjos de forma similar a funções que operam com números naturais. \pause Considere a seguinte definição de lista: \pause

Um arranjo é:

- Vazio; ou

- Um elemento seguido de um arranjo (resto do arranjo)

\pause

Assim como a definição de número natural, essa definição de arranjo também tem autorreferência (é indutiva). \pause

Portanto, para implementar uma função que processa um arranjo, podemos usar a mesma estratégia que usamos para implementar funções recursivas que processam números naturais.


# Exemplo: soma

Projete uma função recursiva que some os elementos de uma lista.


# Exemplo: soma

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def soma(lst: list[int]) -> int:
    '''
    Soma os elementos de *lst*.
    Exemplos
    >>> soma([])
    0
    >>> soma([6])
    6
    >>> soma([3, 6])
    9
    >>> soma([7, 3, 6])
    16
    '''
    return 0

```
</div>
<div class="column" width="48%">
\pause

\small
Como a definição de lista tem dois casos, vamos começar a implementação da função com dois casos. \pause

\scriptsize

```python
if lst == []:
    ...
else:
    # as partes de lst
    lst[0] ... lst[1:]
```

\pause
\small
Como o segundo caso da definição de lista tem uma autorreferência, isto é, `lst[1:]`{.python} é uma lista, vamos fazer uma chamada recursiva para `lst[1:]`{.python}. \pause

\scriptsize

```python
else:
    lst[0] ... soma(lst[1:])
```
</div>
</div>


# Exemplo: soma

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def soma(lst: list[int]) -> int:
    '''
    Soma os elementos de *lst*.
    Exemplos
    >>> soma([])
    0
    >>> soma([6])
    6
    >>> soma([3, 6])
    9
    >>> soma([7, 3, 6])
    16
    '''
```

</div>
<div class="column" width="48%">

\scriptsize

```python
def soma(lst: list[int]) -> int:
    if lst == []:
        # Qual é a soma dos elementos
        # de uma lista vazia?
        s = ...
    else:
        # Sabendo a soma do resto da lista
        # e o valor do primeiro elemento,
        # como obter a soma da lista?
        s = lst[0] ... soma(lst[1:])
    return s
```

</div>
</div>


# Exemplo: soma

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def soma(lst: list[int]) -> int:
    '''
    Soma os elementos de *lst*.
    Exemplos
    >>> soma([])
    0
    >>> soma([6])
    6
    >>> soma([3, 6])
    9
    >>> soma([7, 3, 6])
    16
    '''
```

</div>
<div class="column" width="48%">

\scriptsize

```python
def soma(lst: list[int]) -> int:
    if lst == []:
        # Qual é a soma dos elementos
        # de uma lista vazia?
        s = 0
    else:
        # Sabendo a soma do resto da lista
        # e o valor do primeiro elemento,
        # como obter a soma da lista?
        s = lst[0] + soma(lst[1:])
    return s
```

</div>
</div>


# Exemplo: contagem

Projete uma função recursiva que conte quantas vezes um determinado número aparece em uma lista de números.


# Exemplo: contagem

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def freq(v: int, lst: list[int]) -> int:
    '''
    Conta quantas vezes *v* aparece
    em *lst*.

    Exemplos
    >>> freq(1, [])
    0
    >>> freq(1, [7])
    0
    >>> freq(1, [1, 7, 1])
    2
    >>> freq(4, [4, 1, 7, 4, 4])
    3
    '''
    return 0
```
</div>
<div class="column" width="48%">
\pause

\small
Como a definição de lista tem dois casos, vamos começar a implementação da função com dois casos. \pause

\scriptsize

```python
if lst == []:
    v ...
else:
    # v e as partes de lst
    v ... lst[0] ... lst[1:]
```

\pause
\small
Como o segundo caso da definição de lista tem uma autorreferência, isto é, `lst[1:]`{.python} é uma lista, vamos fazer uma chamada recursiva para `lst[1:]`{.python}. \pause

\scriptsize

```python
else:
    v ... lst[0] ... freq(v, lst[1:])
```
</div>
</div>


# Exemplo: contagem

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def freq(v: int, lst: list[int]) -> int:
    '''
    Conta quantas vezes *v* aparece
    em *lst*.

    Exemplos
    >>> freq(1, [])
    0
    >>> freq(1, [7])
    0
    >>> freq(1, [1, 7, 1])
    2
    >>> freq(4, [4, 1, 7, 4, 4])
    3
    '''
```

</div>
<div class="column" width="48%">
\scriptsize

```python
def freq(v: int, lst: list[int]) -> int:
    if lst == []:
        # Quantas vezes v aparece
        # na lista vazia?
        cont = v ...
    else:
        # Sabendo a quantidade de vezes
        # que v aparece em lst[1:],
        # como determinar a quantidade
        # de vezes que v aparece em lst?
        cont = ...
        v ... lst[0] ... freq(v, lst[1:])
    return cont
```

</div>
</div>


# Exemplo: contagem

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def freq(v: int, lst: list[int]) -> int:
    '''
    Conta quantas vezes *v* aparece
    em *lst*.

    Exemplos
    >>> freq(1, [])
    0
    >>> freq(1, [7])
    0
    >>> freq(1, [1, 7, 1])
    2
    >>> freq(4, [4, 1, 7, 4, 4])
    3
    '''
```

</div>
<div class="column" width="48%">
\scriptsize

```python
def freq(v: int, lst: list[int]) -> int:
    if lst == []:
        # Quantas vezes v aparece
        # na lista vazia?
        cont = 0
    else:
        # Sabendo a quantidade de vezes
        # que v aparece em lst[1:],
        # como determinar a quantidade
        # de vezes que v aparece em lst?
        if v == lst[0]:
            cont = 1 + freq(v, lst[1:])
        else:
            cont = freq(v, lst[1:])
    return cont
```

</div>
</div>


# Exemplo: ordem

Projete uma função recursiva que verifique se os elementos de uma lista estão em ordem não decrescente.


# Exemplo: ordem

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def em_ordem(lst: list[int]) -> bool:
    '''
    Produz True se os elementos de *lst* estão
    em ordem não decrescente, False caso
    contrário.
    Exemplos
    >>> em_ordem([])
    True
    >>> em_ordem([3])
    True
    >>> em_ordem([3, 4])
    True
    >>> em_ordem([4, 3])
    False
    >>> em_ordem([3, 3, 5, 6, 6])
    True
    >>> em_ordem([3, 3, 5, 4, 6])
    False
    '''
    return False
```
</div>
<div class="column" width="48%">
\pause

\small
Como a definição de lista tem dois casos, vamos começar a implementação da função com dois casos. \pause

\scriptsize

```python
if lst == []:
    ...
else:
    # as partes de lst
    lst[0] ... lst[1:]
```

\pause
\small
Como o segundo caso da definição de lista tem uma autorreferência, isto é, `lst[1:]`{.python} é uma lista, vamos fazer uma chamada recursiva para `lst[1:]`{.python}. \pause

\scriptsize

```python
else:
    lst[0] ... em_ordem(lst[1:])
```
</div>
</div>


# Exemplo: ordem

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def em_ordem(lst: list[int]) -> bool:
    '''
    Produz True se os elementos de *lst* estão
    em ordem não decrescente, False caso
    contrário.
    Exemplos
    >>> em_ordem([])
    True
    >>> em_ordem([3])
    True
    >>> em_ordem([3, 4])
    True
    >>> em_ordem([4, 3])
    False
    >>> em_ordem([3, 3, 5, 6, 6])
    True
    >>> em_ordem([3, 3, 5, 4, 6])
    False
    '''
```
</div>
<div class="column" width="48%">

\scriptsize

```python
if lst == []:
    # Os elementos de uma lista
    # vazia estão em ordem?
    ordem = ...
else:
    # Sabendo se os elementos de lst[1:]
    # estão em ordem, como determinar
    # se lst está em ordem?
    ordem = ...
    lst[0] ... em_ordem(lst[1:])
return ordem
```
</div>
</div>


# Exemplo: ordem

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def em_ordem(lst: list[int]) -> bool:
    '''
    Produz True se os elementos de *lst* estão
    em ordem não decrescente, False caso
    contrário.
    Exemplos
    >>> em_ordem([])
    True
    >>> em_ordem([3])
    True
    >>> em_ordem([3, 4])
    True
    >>> em_ordem([4, 3])
    False
    >>> em_ordem([3, 3, 5, 6, 6])
    True
    >>> em_ordem([3, 3, 5, 4, 6])
    False
    '''
```
</div>
<div class="column" width="48%">

\scriptsize

```python
if lst == []:
    # Os elementos de uma lista
    # vazia estão em ordem?
    ordem = True
else:
    # Sabendo se os elementos de lst[1:]
    # estão em ordem, como determinar
    # se lst está em ordem?
    if len(lst) == 1:
        ordem = True
    else:
        ordem = lst[0] <= lst[1] and em_ordem(lst[1:])
return ordem
```

\pause

\normalsize

Podemo simplificar? \pause Sim! \pause

\scriptsize

```python
return len(lst) < 2 or \
           lst[0] <= lst[1] and em_ordem(lst[1:])
```

</div>
</div>


# Diminuição lógica

Apesar das funções `soma`, `freq` e `em_ordem` funcionarem corretamente, elas não são eficientes. \pause

Isto porque a operação de slice (`lst[1:]`{.python}) cria uma nova lista copiando todos os elementos da lista a partir do índice 1, ou seja, estamos diminuindo a lista (problema) fisicamente. \pause

Para resolver esse problema, podemos diminuir a lista de **forma lógica ao invés de forma física**. \pause

A ideia é usar um parâmetro extra `i` que indica de onde a soma deve começar. Na primeira chamada `i = 0`{.python}, na chamada recursiva usamos `i + 1`{.python}. O caso base é atingindo quando `i == len(lst)`{.python}.


# Exemplo: soma com índice incrementando

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def soma_inc(lst: list[int], i: int) -> int:
    '''
    Soma os elementos de *lst* a partir
    de *i*, isto é, soma os elementos
    de *lst[i:]*.
    Requer que 0 <= i <= len(lst).
    >>> soma_inc([7, 3, 6], 0)
    16
    >>> soma_inc([7, 3, 6], 1)
    9
    >>> soma_inc([7, 3, 6], 2)
    6
    >>> soma_inc([7, 3, 6], 3)
    0
    '''
```

\pause

</div>
<div class="column" width="48%">
\scriptsize

```python
def soma_inc(lst: list[int], i: int) -> int:
    if i >= len(lst):
        # Qual é a soma dos elementos
        # de lst a partir de i?
        s = 0
    else:
        # Tendo a soma dos elementos de
        # lst a partir de i + 1 (chamada
        # recursiva) e lst[i], como
        # obter a soma dos elementos
        # de lst a partir de i?
        s = lst[i] + soma_inc(lst, i + 1)
    return s
```
</div>
</div>


# Exemplo: soma com índice decrementando

Ao invés de começar o parâmetro extra com 0 e incrementar na chamada recursiva, podemos começar com `len(lst)`{.python} e decrementar na chamada recursiva. \pause

Desse forma, o parâmetro extra funciona como um **tamanho lógico** para `lst` e podemos pensar em recursão com lista da mesma forma que pensamos em recursão com número natural. \pause

Vamos chamar o parâmetro de `n` ao invés de `i` para destacar a relação com o tamanho.


# Exemplo: soma com índice decrementando

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def soma_dec(lst: list[int], n: int) -> int:
    '''
    Soma os primeiro *n* elementos de *lst*,
    isto é, soma os elementos de *lst[:n]*.
    Requer que 0 <= n <= len(lst)
    >>> soma_dec([7, 3, 6], 0)
    0
    >>> soma_dec([7, 3, 6], 1)
    7
    >>> soma_dec([7, 3, 6], 2)
    10
    >>> soma_dec([7, 3, 6], 3)
    16
    '''
```

\pause

</div>
<div class="column" width="48%">
\scriptsize

```python
def soma_dec(lst: list[int], n: int) -> int:
    if n == 0:
        # Qual é a soma de lst, sendo
        # que o "tamanho" (n) de lst é 0?
        s = 0
    else:
        # Tendo a soma dos elementos
        # de lst sem o "último" elemento
        # de lst (chamada recursiva)
        # e o último elemento (lst[n-1]),
        # como obtemos a soma de todos os
        # elementos de lst[:n]?
        s = lst[n - 1] + soma_dec(lst, n - 1)
    return s
```
</div>
</div>


# Limitações

A técnica de diminuição e conquista sempre funciona? \pause Ou seja, se aplicarmos a ideia de diminuir e conquistar conseguimos projetar um algoritmo para resolver qualquer problema? \pause

Não! \pause

Mas então, quando podemos aplicar a técnica de projeto de diminuição e conquista? \pause

- Quando conseguimos resolver o caso base; \pause

- Quando a solução do problema menor pode ser estendida para a solução do problema inicial.


# Limitações

Podemos aplicar a técnica de diminuição e conquista para projetar uma função que encontre todos os divisores de um número natural $n$? \pause

Conseguimos resolver o caso base? \pause Sim. \pause

Tendo os divisores de $n - 1$, podemos encontrar os divisores de $n$? \pause Sabendo os divisores de $9\ (1, 3, 9)$, podemos determinar os divisores de $10\ (1, 2, 5, 10)$? \pause Não! \pause

Ou seja, a solução do problema menor não pode ser estendida para o problema inicial. \pause

Vocês verão em outras disciplinas outras estratégias que permitirão superar essa limitação.


# Revisão

Definições recursivas são aquelas feitas em termos de si mesmas. Para ser bem formada uma definição recursiva precisa de: \pause

- Pelo menos um caso base; \pause
- Pelo menos um caso com autorreferência. \pause

Funções recursivas são aquelas que chamam a si mesmas. Para ser bem formada uma função recursiva precisa de: \pause

- Pelo menos um caso base; \pause
- Pelo menos um caso com chamada recursiva.


# Revisão

Vimos como empregar definições e funções recursivas para projetar funções utilizando a técnica de diminuição e conquista. \pause

A ideia é diminuir o problema inicial, conquistar o problema menor -- diretamente ou recursivamente -- e estender a solução do problema menor para o problema inicial. \pause

A forma mais direta de diminuir um problema é explorar a relação entre autorreferência na definição do tipo de dado e recursão na função: onde tem autorreferência tem recursão.


# Revisão

Aplicamos essa forma de diminuir o problema tanto para números naturais quanto para arranjos. \pause

Para arranjos usamos diminuição lógica para para evitar que arranjos sejam criados com a operação de subarranjo (`[1:]`) nas chamadas recursivas. \pause Fizemos a diminuição a partir do início e do fim. \pause

A estratégia de diminuição e conquista não pode ser usada para resolver qualquer problema. \pause Se não conseguimos definir como diminuir o problema ou estender a solução do problema menor para o problema inicial, então não podemos utilizar a técnica de diminuição e conquista.
