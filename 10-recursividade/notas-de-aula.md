---
# vim: set spell spelllang=pt_br:
title: Recursividade
---

# Introdução

Nós vimos como a definição de tipos de dados adequadas é importante no projeto de programas. \pause

Agora vamos explorar como a forma da definição do tipo de dado pode nos ajudar a escrever o corpo das funções.


# Número natural

Considere a seguinte definição de número natural: \pause

- $0$ é um número natural; \pause
- Se $n$ é um número natural, então $n + 1$ é um número natural. \pause

O que esta definição tem de diferente? \pause

No segundo caso, um número natural é definido em termos de outro número natural! \pause Como isso é possível!?


# Definições recursivas

Como é possível definir uma coisa em termos dela mesmo? \pause

Este tipo de definição é chamada de **definição recursiva** (ou definição indutiva) e é muito utilizada na computação e matemática. \pause

Para ser válida, uma definição recursiva precisa de\pause

- Pelo menos um caso base (que não depende da própria definição) \pause
- Pelo menos um caso com autorreferência (que depende da própria definição para elementos "menores") \pause

A partir do(s) caso(s) base, os outros elementos são definidos de forma indutiva pelos casos com autorreferência.


# Definições recursivas

<div class="columns">
<div class="column" width="45%">

\small

Definição de número natural:

- $0$ é um número natural; \pause
- Se $n$ é um número natural, então $n + 1$ é um número natural. \pause

</div>
<div class="column" width="48%">

\small

O número 4 é natural? \pause Vamos verificar \pause

- Como 4 não é zero, para ele ser natural, o 3 tem que ser natural \pause
- Como 3 não é zero, para ele ser natural, o 2 tem que ser natural \pause
- Como 2 não é zero, pare ele ser natural, o 1 tem que ser natural \pause
- Como 1 não é zero, pare ele ser natural, o 0 tem que ser natural \pause
- Por definição, 0 é natural \pause

Portanto, o 4 é natural. \pause

Note que foi preciso decompor o 4 até chegar no caso base.

</div>
</div>


# Funções

Assim como temos definições recursivas, também podemos ter funções recursivas. \pause

Uma **função recursiva** é aquela que chama a si mesmo. \pause

Assim como para definições recursivas, para estar bem formada uma função recursiva precisa de \pause

- Pelo menos um caso base (o valor da função é calculado diretamente) \pause
- Pelo menos um caso com chamada recursiva (depende do valor da função para entradas menores)


# Projeto de funções recursivas

Como projetar funções recursivas? \pause

Existem várias técnicas de projeto de funções recursivas, nós vamos explorar uma delas, chamada de diminuição e conquista. \pause

A ideia é diminuir o tamanho do problema original, conquistar o problema menor -- diretamente ou recursivamente, e estender a solução do problema menor para o problema original. \pause

No início, para diminuir o problema original, nós vamos explorar a relação entre autorreferência na definição do tipo de dado e a chamada recursiva na função que processa o tipo de dado.


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
        # como obter a soma para os
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
        # como obter a soma para os
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


# Exemplo: fatorial

Projete uma função recursiva que calcule o fatorial de $n$, isto é, o produto dos $n$ primeiros números naturais maiores que $0$.


# Exemplo: fatorial

<div class="columns">
<div class="column" width="45%">
\scriptsize

```python
def fatorial(n: int) -> int:
    '''
    Calcula o fatorial de *n*, isto é,
    o produto dos *n* primeiros números
    naturais maiores que 0.
    Requer que n >= 0.
    Exemplos
    >>> fatorial(0)
    1
    >>> fatorial(1)
    1
    >>> fatorial(2)
    2
    >>> fatorial(3)
    6
    >>> fatorial(4)
    24
    '''
    return 0
```

</div>
<div class="column" width="52%">
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
    n ... fatorial(n - 1)
```

</div>
</div>


# Exemplo: fatorial

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def fatorial(n: int) -> int:
    '''
    Calcula o fatorial de *n*, isto é,
    o produto dos *n* primeiros números
    naturais maiores que 0.
    Requer que n >= 0.
    Exemplos
    >>> fatorial(0)
    1
    >>> fatorial(1)
    1
    >>> fatorial(2)
    2
    >>> fatorial(3)
    6
    >>> fatorial(4)
    24
    '''
```

</div>
<div class="column" width="48%">

\scriptsize

```python
def fatorial(n: int) -> int:
    if n == 0:
        # Qual é o fatorial de 0,
        # isto é, o produto dos
        # primeiros n == 0
        # naturais maiores que 0?
        fat = ...
    else:
        # Tendo o fatorial de n - 1
        # e o natural n, como obter
        # o fatorial de n?
        fat = n ... fatorial(n - 1)
    return fat
```

</div>
</div>


# Exemplo: fatorial

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def fatorial(n: int) -> int:
    '''
    Calcula o fatorial de *n*, isto é,
    o produto dos *n* primeiros números
    naturais maiores que 0.
    Requer que n >= 0.
    Exemplos
    >>> fatorial(0)
    1
    >>> fatorial(1)
    1
    >>> fatorial(2)
    2
    >>> fatorial(3)
    6
    >>> fatorial(4)
    24
    '''
```

</div>
<div class="column" width="48%">

\scriptsize

```python
def fatorial(n: int) -> int:
    if n == 0:
        # Qual é o fatorial de 0,
        # isto é, o produto dos
        # primeiros n == 0
        # naturais maiores que 0?
        fat = 1
    else:
        # Tendo o fatorial de n - 1
        # e o natural n, como obter
        # o fatorial de n?
        fat = n * fatorial(n - 1)
    return fat
```

</div>
</div>



# Aspectos importantes no projeto de funções recursivas

Quando estamos projetando funções recursivas, temos que considerar dois aspectos: \pause

- A chamada recursiva deve ser feita para uma **entrada "menor"**, dessa forma temos a certeza que o caso base será alcançado e a função terminará. \pause

- Devemos **confiar na chamada recursiva**, isto é, que ela produz a resposta correta, e nos preocuparmos apenas em como utilizar essa resposta para calcular o resultado da função.


# Funções recursivas com arranjos

Podemos projetar funções recursivas que operam em listas de forma similar a funções que operam com números naturais. \pause Considere a seguinte definição de lista: \pause

Uma lista é:

- Vazia; ou

- Um elemento seguido de uma lista (resto da lista)

\pause

Assim como a definição de número natural, essa definição de lista também tem autorreferência (é indutiva). \pause

Portanto, para implementar uma função que processa uma lista, podemos usar a mesma estratégia que usamos para implementar funções recursivas que processam números naturais. \pause

Vamos ver alguns exemplos.


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
        # como determinamos a quantidade
        # de vezes que v aparece em lst?
        cont = ...
        v... lst[0] ... freq(v, lst[1:])
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
        cont = ...
    else:
        # Sabendo a quantidade de vezes
        # que v aparece em lst[1:],
        # como determinamos a quantidade
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


# Diminuição e conquista

Esta técnica sempre funciona? Ou seja, se eu aplicar a ideia de diminuir e conquistar eu consigo projetar um algoritmo para resolver qualquer problema? \pause

Não! \pause

Mas então, quando podemos aplicar a técnica de projeto diminuição e conquista? \pause

- Quando conseguimos resolver o caso base \pause

- Quando a solução do problema menor pode ser estendida para a solução do problema original


# Diminuição e conquista

Se quisermos encontrar todos os divisores de um número $n$, podemos aplicar essa técnica? \pause

Conseguimos resolver o caso base? \pause Sim. \pause

Tendo os divisores de $n - 1$, podemos encontrar os divisores de $n$? \pause Sabendo os divisores de $9 (1, 3, 9)$, podemos determinar os divisores de $10 (1, 2, 5, 10)$? \pause Não! \pause

Então essa técnica não é adequada para esse problema.


# Variantes

Podemos diminuir as listas de outra forma que não seja "removendo" o primeiro? \pause

Sim, podemos "remover" o último. \pause

Também podemos remover qualquer quantidade do início e/ou do fim.
